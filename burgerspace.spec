Name:		burgerspace
Version:	1.9.3
Release:	2
Summary:	A Burgertime(TM) clone
License:	GPLv2+
Group:		Games/Arcade
URL:		https://sarrazip.com/dev/burgerspace.html
Source0: 	http://perso.b2b2c.ca/~sarrazip/dev/%{name}-%{version}.tar.gz
Source1:	%{name}-16x16.png
Source2:	%{name}-32x32.png
Source3:	%{name}-48x48.png
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	flatzebra-devel >= 0.1.5
# this one is really needed only in 2011
#BuildRequires:	libstdc++-static-devel

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
%makeinstall_std

#icon
%__mkdir_p %{buildroot}%{_iconsdir}
%__mkdir_p %{buildroot}%{_miconsdir}
%__mkdir_p %{buildroot}%{_liconsdir}
cp %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png
cp %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
cp %{SOURCE3} %{buildroot}%{_liconsdir}/%{name}.png

%__rm -fr %{buildroot}%{_defaultdocdir}/%{name}-*

%files
%doc AUTHORS COPYING  INSTALL NEWS README THANKS TODO
%{_bindir}/burgerspace
%{_bindir}/burgerspace-server
%{_datadir}/sounds/*
%{_mandir}/man6/burgerspace.6*
%{_mandir}/man6/burgerspace-server.6*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
