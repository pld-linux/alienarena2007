%define		relyear		2007
%define		dateversion	20070613
#
Summary:	Alien Arena - freeware online deathmatch FPS game
Summary(pl.UTF-8):Alien Arena
Name:		alienarena%{relyear}
Version:	6.10
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://gd.tuwien.ac.at/opsys/linux/gentoo/distfiles/%{name}-%{dateversion}-linux.zip
# Source0-md5:	65d2948fa636cbc28c82da2264df2fea
URL:		http://red.planetarena.org/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	dos2unix
BuildRequires:	libjpeg-devel
BuildRequires:	SDL-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ALIEN ARENA is a standalone 3D first person online deathmatch shooter
crafted from the original source code of Quake II and Quake III,
released by id Software under the GPL license. With features including
32 bit graphics, new particle engine and effects, light blooms,
reflective water, hi resolution textures and skins, hi poly models,
stain maps, ALIEN ARENA pushes the envelope of graphical beauty
rivaling today's top games.

The game features 37 levels, which can be played online against other
players, or against the built in CodeRED bots.

Alien Arena offers CTF, AOA(All Out Assault) mode, in which players
can climb into vehicles to do battle, Deathball, and Team Core
Assault. Simply go into the multiplayer menu to start a server, change
the game rules, and choose a map to play on. You can also select from
five different mutators(instagib, rocket arena, excessive, low grav,
regen, and vampire) to further customize your game experience.

%package server
Summary:	Alien Arena - server
Summary(pl.UTF-8):Alien Arena - serwer
Group:		X11/Applications/Games

%description server
The dedicated server for Alien Arena.

%package data
Summary:	Alien Arena - the data, botinfo, and arena files
Group:		X11/Applications/Games

%description data
This package installs the data, botinfo, and arena files needed to run
Alien Arena.

%prep
%setup -q -n %{name}
rm -f ../GH3D.txt ../GamersHell.url

for file in lst cfg txt html lng h c ; do
        find ./ -noleaf -type f -name \*.$file -exec dos2unix '{}' \;
done

%build
%{__make} \
	CFLAGS="%{rpmcflags} -ldl" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun server
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi

%files
%defattr(644,root,root,755)
%doc changelog README
%lang(du) %doc docs/AA Dutch.txt
%lang(fr) %doc docs/AA French.txt
%lang(de) %doc docs/AA German.txt
%lang(gr) %doc docs/AA Greek.txt
%lang(hu) %doc docs/AA Hungarian.txt
%lang(it) %doc docs/AA Italian.txt
%lang(pl) %doc docs/AA Polish.txt
%lang(po) %doc docs/AA Portuguese.txt
%lang(ru) %doc docs/AA Russian.txt
%lang(es) %doc docs/AA_ES.txt
%attr(755,root,root) %{_bindir}/alien-arena
%{_desktopdir}/alien-arena.desktop
%{_pixmapsdir}/alien-arena.xpm

%files data
%defattr(644,root,root,755)

%files server
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(755,root,root) %{_bindir}/alien-arena-server
alien-arena/crded
alien-arena/kill-runaway-crded
alien-arena/launch-server
alien-arena/rcon
alien-arena/svstat
%{_mandir}/man6/alien-arena-server.6.*
