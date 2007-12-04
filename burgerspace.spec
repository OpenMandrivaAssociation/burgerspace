%define name	burgerspace
%define version 1.8.1
%define release  %mkrel 1

Summary:	A Burgertime(TM) clone
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{name}-%{version}.tar.bz2
Source1:	%{name}-16x16.png.bz2
Source2:	%{name}-32x32.png.bz2
Source3:	%{name}-48x48.png.bz2
License:	GPL
URL:		http://www3.sympatico.ca/sarrazip/dev/burgerspace.html
Group:		Games/Arcade
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig
BuildRequires:	SDL1.2-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:  SDL_mixer-devel >= 1.2.0
BuildRequires:	flatzebra-devel >= 0.1.1

%description
Clone of the Burgertime video game.  You are a chef that must walk
over hamburger ingredients in a maze while avoiding enemies.

Use the arrow keys to move, the left Ctrl key to throw pepper, and 
P to pause the game and resume it. The Escape key quits the game.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --datadir=%{_datadir} \
	--libdir=%{_libdir} --mandir=%{_mandir}
%make
# CXXFLAGS="-DNDEBUG -O2"

%install
 [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
 && rm -rf ${RPM_BUILD_ROOT}/
 
make DESTDIR=$RPM_BUILD_ROOT install

# Menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/%{name}" needs="X11" \
icon="%{name}.png" section="Amusement/Arcade" \
title="Burgerspace" longtitle="Burgerspace is a Burgertime(TM) clone"
EOF
  
#icon
install -d $RPM_BUILD_ROOT/%{_iconsdir}
install -d $RPM_BUILD_ROOT/%{_miconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
bzcat %{SOURCE1} > $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus}

%clean
 [ -n "${RPM_BUILD_ROOT}" -a "${RPM_BUILD_ROOT}" != / ] \
 && rm -rf ${RPM_BUILD_ROOT}/

%files
%defattr(-, root, root)
%doc AUTHORS COPYING HACKING INSTALL NEWS README THANKS TODO
%{_bindir}/burgerspace
%{_datadir}/sounds/*
%{_mandir}/man6/burgerspace.6*
%{_menudir}/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%_datadir/applications/*
%_datadir/pixmaps/*.png 
 

