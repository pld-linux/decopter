%define		_textures_ver	0.2.7
Summary:	Unrealistic helicopter simulator
Summary(pl):	Nierealistyczny symulator helikoptera
Name:		decopter
Version:	0.2.9
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	http://dl.sourceforge.net/%{name}/%{name}-textures-%{_textures_ver}.tar.gz
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		%{name}-paths.patch
URL:		http://decopter.sourceforge.net/
Buildrequires:	OpenGL-devel
BuildRequires:	SDL-devel
Buildrequires:	SDL_image-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
decopter is an unrealistic helicopter simulator. It is not playable,
you can just fly around.

%description -l pl
decopter jest nierealistycznym symulatorem helikoptera. Nie jest on
grywalny, mo¿na tylko lataæ w ko³o.

%prep
%setup -q -a 1
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Games,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{3D,desc,maps,textures}

install fly $RPM_BUILD_ROOT%{_bindir}/decopter
install generate_textures $RPM_BUILD_ROOT%{_bindir}
install landscape_texture_browser $RPM_BUILD_ROOT%{_bindir}

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
