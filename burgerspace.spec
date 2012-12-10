Name:		burgerspace
Version:	1.9.1
Release:	1
Summary:	A Burgertime(TM) clone
License:	GPLv2+
Group:		Games/Arcade
URL:		http://sarrazip.com/dev/burgerspace.html
Source0: 	http://perso.b2b2c.ca/sarrazip/dev/%{name}-%{version}.tar.gz
Source1:	%{name}-16x16.png.bz2
Source2:	%{name}-32x32.png.bz2
Source3:	%{name}-48x48.png.bz2
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
bzcat %{SOURCE1} > %{buildroot}%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > %{buildroot}%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > %{buildroot}%{_liconsdir}/%{name}.png

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


%changelog
* Tue Mar 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.9.0-1mdv2011.0
+ Revision: 784504
- Update BuildRequires

* Mon Mar 12 2012 Andrey Bondrov <abondrov@mandriva.org> 1.9.0-1
+ Revision: 784464
- Update file list
- New version 1.9.0, spec cleanup, update BuildRequires

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Sat Jul 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.3-2mdv2010.0
+ Revision: 399810
- fix dependencies
- spec cleanup

* Fri May 15 2009 Samuel Verschelde <stormi@mandriva.org> 1.8.3-1mdv2010.0
+ Revision: 376196
- new version 1.8.3
- fix licence
- remove redundant desktop file
- add requires

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Dec 27 2007 Jérôme Soyer <saispo@mandriva.org> 1.8.2-1mdv2008.1
+ Revision: 138360
- New release

  + Nicolas Vigier <nvigier@mandriva.com>
    - fix URL

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 1.8.1-1mdv2008.1
+ Revision: 132294
- auto-convert XDG menu entry
- fix build
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- fix hardcoded man page extension
- import burgerspace


* Thu May 05 2005 Marcel Pol <mpol@mandriva.org> 1.8.1-1mdk
- 1.8.1
- adjust buildrequires

* Sat Aug 28 2004 Marcel Pol <mpol@mandrake.org> 1.8.0-4mdk
- rebuild to fix menu (#11013)

* Sat Jun 05 2004 Marcel Pol <mpol@mandrake.org> 1.8.0-3mdk
- rebuild

* Thu Jun 12 2003 Marcel Pol <mpol@gmx.net> 1.8.0-2mdk
- buildrequires

* Tue Jun 03 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.8.0-1mdk
- 1.8.0

* Thu Jan 23 2003 Marcel Pol <mpol@gmx.net> 1.7.1-1mdk
- 1.7.1

* Tue Jan 15 2002 Marcel Pol <mpol@gmx.net> 1.6-1mdk
- Mandrake build
- s/Copyright/License
- BuildRequires libgengameng4-devel libSDL1.2-devel libSDL_image1.2
- added menu-entry with icons
 
