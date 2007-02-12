# TODO:
# 1a) make textures system-wide and generate them in %post
#      -- or --
# 1b) run generate_textures automagically when no textures for current user
#     found
#  2) possibly move generate_textures to %{_libdir} or make its name less
#     general
#
%define		_textures_ver	0.2.7
Summary:	Unrealistic helicopter simulator
Summary(pl.UTF-8):   Nierealistyczny symulator helikoptera
Name:		decopter
Version:	0.2.11
Release:	2.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/decopter/%{name}-%{version}.tar.gz
# Source0-md5:	802d2fe2f187bab388ef2f9fd37871c8
Source1:	http://dl.sourceforge.net/decopter/%{name}-textures-%{_textures_ver}.tar.gz
# Source1-md5:	95b1311447f1ec91869986550dc9d33b
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-paths.patch
Patch1:		%{name}-c++.patch
URL:		http://decopter.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
decopter is an unrealistic helicopter simulator. It is not playable,
you can just fly around.

%description -l pl.UTF-8
decopter jest nierealistycznym symulatorem helikoptera. Nie jest on
grywalny, można tylko latać w koło.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="`sdl-config --cflags` -Wall %{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
	LDFLAGS="`sdl-config --libs` -lSDL_image -lGL -lGLU -lstdc++"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{3D,desc,maps,textures}

install fly $RPM_BUILD_ROOT%{_bindir}/decopter
install generate_textures $RPM_BUILD_ROOT%{_bindir}

install 3D/* $RPM_BUILD_ROOT%{_datadir}/%{name}/3D
install desc/* $RPM_BUILD_ROOT%{_datadir}/%{name}/desc
install maps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/maps
install textures/* $RPM_BUILD_ROOT%{_datadir}/%{name}/textures

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "NOTE: Run generate_textures before first play"

%files
%defattr(644,root,root,755)
%doc BUGS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
