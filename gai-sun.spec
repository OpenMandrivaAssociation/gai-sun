%define name gai-sun
%define version 0.1
%define release %mkrel 6

Name: %name
Summary: Tells you when the Sun rises and set at a place on earth
Version: %{version}
Release: %{release}
License: GPL
Url: http://gai.sf.net
Group: Games/Other
Source: %{name}-%{version}.tar.bz2
Source10:   %{name}-16.png
Source11:   %{name}-32.png
Source12:   %{name}-48.png
BuildRoot: %{_tmppath}/build-root-%{name}

BuildRequires: automake >= 1.4
BuildRequires: libgai-devel >= 0.5

%description
A simple applet that displays the time when they sun sets and rises.
Based upon wmSun.

%prep
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
%setup -q 

%build
%configure
%make 

%install
rm -rf ${RPM_BUILD_ROOT}
install -m755 %name -D $RPM_BUILD_ROOT%{_bindir}/%name
install -m644 GNOME_DefaultApplet.server -D $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/GNOME_%{name}Applet.server
install -m644 %name-icon.png -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%name-icon.png
mkdir $RPM_BUILD_ROOT%{_datadir}/pixmaps/%name
cp images/* $RPM_BUILD_ROOT%{_datadir}/pixmaps/%name
install -m644 %SOURCE10 -D %{buildroot}/%_miconsdir/%name.png
install -m644 %SOURCE11 -D %{buildroot}/%_iconsdir/%name.png
install -m644 %SOURCE12 -D %{buildroot}/%_liconsdir/%name.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gai-sun
Comment=Display time when they sun sets and rise
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Toys;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root,0755)
%doc INSTALL README README.gai
%{_bindir}/*
%{_libdir}/bonobo/servers/GNOME_%{name}Applet.server
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/pixmaps/*
%{_iconsdir}/%name.png
%{_liconsdir}/%name.png
%{_miconsdir}/%name.png


