%define		_textures_ver	0.2.7
Summary:	Unrealistic helicopter simulator
Summary(pl):	Nierealistyczny symulator helikoptera
Name:		decopter
Version:	0.2.11
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	802d2fe2f187bab388ef2f9fd37871c8
Source1:	http://dl.sourceforge.net/%{name}/%{name}-textures-%{_textures_ver}.tar.gz
# Source1-md5:	95b1311447f1ec91869986550dc9d33b
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-paths.patch
Patch1:		%{name}-c++.patch
URL:		http://decopter.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
decopter is an unrealistic helicopter simulator. It is not playable,
you can just fly around.

%description -l pl
decopter jest nierealistycznym symulatorem helikoptera. Nie jest on
grywalny, mo�na tylko lata� w ko�o.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="`sdl-config --cflags` -I/usr/X11R6/include -Wall %{rpmcflags} %{!?debug:-fomit-frame-pointer}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Games,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{3D,desc,maps,textures}

install fly $RPM_BUILD_ROOT%{_bindir}/decopter
install generate_textures $RPM_BUILD_ROOT%{_bindir}

install 3D/* $RPM_BUILD_ROOT%{_datadir}/%{name}/3D
install desc/* $RPM_BUILD_ROOT%{_datadir}/%{name}/desc
install maps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/maps
install textures/* $RPM_BUILD_ROOT%{_datadir}/%{name}/textures

install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games
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
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
