Name:		burgerspace
Version:	1.9.0
Release:	%mkrel 1
Summary:	A Burgertime(TM) clone
License:	GPLv2+
Group:		Games/Arcade
URL:		http://sarrazip.com/dev/burgerspace.html
Source0: 	http://perso.b2b2c.ca/sarrazip/dev/%{name}-%{version}.tar.gz
Source1:	%{name}-16x16.png.bz2
Source2:	%{name}-32x32.png.bz2
Source3:	%{name}-48x48.png.bz2
BuildRequires:	SDL1.2-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel >= 1.2.0
BuildRequires:	flatzebra-devel >= 0.1.5

%description
Clone of the Burgertime video game.  You are a chef that must walk
over hamburger ingredients in a maze while avoiding enemies.

Use the arrow keys to move, the left Ctrl key to throw pepper, and
P to pause the game and resume it. The Escape key quits the game.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

#icon
%__mkdir_p %{buildroot}%{_iconsdir}
%__mkdir_p %{buildroot}%{_miconsdir}
%__mkdir_p %{buildroot}%{_liconsdir}
bzcat %{SOURCE1} > %{buildroot}%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > %{buildroot}%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > %{buildroot}%{_liconsdir}/%{name}.png

%__rm -fr %{buildroot}%{_defaultdocdir}/%{name}-*

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS COPYING  INSTALL NEWS README THANKS TODO
%{_bindir}/burgerspace
%{_datadir}/sounds/*
%{_mandir}/man6/burgerspace.6*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png


