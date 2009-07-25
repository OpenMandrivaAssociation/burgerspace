%define name	burgerspace
%define version 1.8.3
%define release  %mkrel 2

Summary:	A Burgertime(TM) clone
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License:	GPLv2+
Group:		Games/Arcade
URL:		http://sarrazip.com/dev/burgerspace.html
Source0: 	http://perso.b2b2c.ca/sarrazip/dev/%{name}-%{version}.tar.gz
Source1:	%{name}-16x16.png.bz2
Source2:	%{name}-32x32.png.bz2
Source3:	%{name}-48x48.png.bz2
BuildRequires:	pkgconfig
BuildRequires:	SDL1.2-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:  SDL_mixer-devel >= 1.2.0
BuildRequires:	flatzebra-devel >= 0.1.2
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Clone of the Burgertime video game.  You are a chef that must walk
over hamburger ingredients in a maze while avoiding enemies.

Use the arrow keys to move, the left Ctrl key to throw pepper, and
P to pause the game and resume it. The Escape key quits the game.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#icon
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}
install -d %{buildroot}%{_liconsdir}
bzcat %{SOURCE1} > %{buildroot}%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > %{buildroot}%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > %{buildroot}%{_liconsdir}/%{name}.png

rm -fr %buildroot/%_defaultdocdir/%name-*

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING  INSTALL NEWS README THANKS TODO
%{_bindir}/burgerspace
%{_datadir}/sounds/*
%{_mandir}/man6/burgerspace.6*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%_datadir/applications/*
%_datadir/pixmaps/*.png


