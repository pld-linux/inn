%include	/usr/lib/rpm/macros.perl
Summary:	INN, the InterNet News System (news server)
Summary(de):	das InterNet News System (News-Server)
Summary(es):	INN, InterNet News System (servidor news)
Summary(fr):	INN, le système InterNet News (serveur de news)
Summary(pl):	INN, serwer nowinek
Summary(pt_BR):	INN, InterNet News System (servidor news)
Summary(tr):	INN, InterNet Haber Sistemi (haber sunucu)
Name:		inn
Version:	2.4.1
Release:	0.5
License:	distributable
Group:		Networking/Daemons
Source0:	ftp://ftp.isc.org/isc/inn/%{name}-%{version}.tar.gz
# Source0-md5:	bec635b6e70188071fdb539cd374f2ba
Source1:	%{name}-default-active
Source2:	%{name}-default-distributions
Source3:	%{name}-default-newsgroups
Source4:	%{name}-etc-%{name}.conf
Source5:	%{name}-etc-newsfeeds
Source6:	%{name}.crontab
Source7:	%{name}.init
Source8:	%{name}-cnfsstat.cron
Source9:	%{name}.logrotate
Source10:	%{name}-etc-readers.conf
Source11:	getlist.1.pl
Source12:	%{name}d.8.pl
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-db.patch
Patch3:		%{name}-ac25x.patch
Patch4:		%{name}-ac253.patch
Patch5:		%{name}-setgid.patch
Patch6:		%{name}-db4.patch
Patch7:		%{name}-timecaf_oversized_art.patch
Patch8:		%{name}-lib_install_modes.patch
Patch9:		%{name}-kill_warnings.patch
Patch10:	%{name}-64bit_pointers.patch
#Patch11:	%{name}-setreuid.patch
#Patch12:	%{name}-sec.patch
#Patch13:	%{name}-frsize.patch
URL:		http://www.isc.org/inn.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	db-devel
BuildRequires:	flex
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
PreReq:		%{name}-libs = %{version}
PreReq:		rc-scripts
Requires(post):	/bin/kill
Requires(post):	/usr/bin/getent
Requires(post,preun):	/sbin/chkconfig
Requires(post):	sed
Requires(post):	fileutils
Requires(post):	textutils
Requires(post):	/usr/sbin/usermod
Requires:	cleanfeed >= 0.95.7b-4
Requires:	rc-scripts >= 0.2.0
Requires:	/etc/cron.d
Requires:	psmisc >= 20.1
Requires:	util-linux
Requires:	procps
Requires:	textutils
Requires:	awk
Provides:	nntpserver
Obsoletes:	leafnode
Obsoletes:	leafnode+
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/news
%define		_includedir	%{_prefix}/include/inn

# /usr/bin/pullnews doesn't provide perl(Net::NNTP) - perl-libnet does.
%define		_noautoprov	'perl(Net::NNTP)'
# it's necessary only for sample nnrpd_auth.pl hook
%define		_noautoreq	'perl(CDB_File)'

%description
INN is a news server, which can be set up to handle USENET news, as
well as private "newsfeeds". There is a *LOT* of information about
setting up INN in /usr/share/doc -- read it.

If you want innreport to generate graphs you need perl-GD package.

%description -l es
INN es un servidor de news, que puede ser configurado para manipular
USENET news bien como newsfeeds privadas. Existe un *Montón* de
información sobre la configuración del INN en /usr/doc -- léela.

%description -l pl
INN jest serwerem news, który mo¿na skonfigurowaæ do obs³ugi USENET-u,
jak równie¿ do obs³ugi ,,prywatnych'' grup w sieciach intranetowych.
Ca³e mnóstwo po¿ytecznych informacji o konfigurowaniu INN-a znajdziesz
w katalogu /usr/share/doc/inn-*.

Je¶li chcesz ¿eby innreport generowa³ wykresy musisz zainstalowaæ
pakiet perl-GD.

%description -l pt_BR
INN é um servidor de news, que pode ser configurado para manipular
USENET news bem como newsfeeds privadas. Existe um *MONTE* de
informações sobre a configuração do INN em /usr/doc -- leia.

%package libs
Summary:	INN libraries
Summary(de):	INN-Library
Summary(fr):	Bibliothèque INN
Summary(pl):	Biblioteki do INN-a
Group:		Development/Libraries

%description libs
This library is needed by several programs that interface to INN, such
as newsgate or tin.

%description libs -l de
Diese Library wird von mehreren Programmen benötigt, die mit INN
kommunizieren, etwa newsgate oder tin.

%description libs -l fr
Cette bibliothèque est nécessaire à plusieurs programmes qui
s'interfacent avec INN, comme newsgate ou tin.

%description libs -l pl
Biblioteka niezbêdna do dzia³ania kilku programów wspó³pracuj±cych z
INN-em, takich jak newsgate czy tin.

%description libs -l tr
INN ile arayüz gerektiren programlar için (newsgate, tin gibi) gereken
bir kitaplýktýr.

%package devel
Summary:	INN header files and development documentations
Summary(de):	INN-Library
Summary(es):	Biblioteca INN
Summary(fr):	Bibliothèque INN
Summary(pl):	Pliki nag³ówkowe i dokumentacja programisty do inn-a
Summary(pt_BR):	Biblioteca INN
Summary(tr):	INN kitaplýðý
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}
Requires:	db-devel

%description devel
Header files and developer documentations for INN libraries.

%description devel -l de
Diese Library wird von mehreren Programmen benötigt, die mit INN
kommunizieren, etwa newsgate oder tin.

%description devel -l es
Esta biblioteca es requerida por varios programas que tienen interface
con INN, como el newsgate o tin.

%description devel -l fr
Cette bibliothèque est nécessaire à plusieurs programmes qui
s'interfacent avec INN, comme newsgate ou tin.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do bibliotek INN-a.

%description devel -l pt_BR
Esta biblioteca é requerida por vários programas que tem interface com
o INN, como o newsgate ou tin.

%description devel -l tr
INN ile arayüz gerektiren programlar için (newsgate, tin gibi) gereken
bir kitaplýktýr.

%package static
Summary:	Static INN libraries
Summary(es):	Static libraries for inn development
Summary(pl):	Biblioteki statyczne do INN
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com inn
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static INN libraries.

%description static -l es
Static libraries for inn development

%description static -l pl
Biblioteki statyczne do INN.

%description static -l pt_BR
INN é um servidor de news, que pode ser configurado para manipular
USENET news bem como newsfeeds privadas. Existe um *MONTE* de
informações sobre a configuração do INN em /usr/doc -- leia.

Bibliotecas estáticas para desenvolvimento com inn

%package -n inews
Summary:	Inews program (used for posting by inn and trn)
Summary(de):	Inews-Programm (für die Zustellung mit inn und trn)
Summary(es):	Programa Inews (usado para franqueo por inn y trn)
Summary(fr):	Programme inews (utilisé par inn et trn pour poster)
Summary(pl):	Inews - program do wysy³ania artyku³ów (u¿ywany przez inn i trn)
Summary(pt_BR):	Programa Inews (usado para postagem pelo inn e trn)
Summary(tr):	Haber biçimlendirme programý
Group:		Networking/News
Requires:	%{name}-libs = %{version}

%description -n inews
The inews program is used by some news readers to post news. It does
some consistency checking and header reformatting, and forwards the
article on to the news server specified in inn.conf.

%description -n inews -l de
Das Programm 'inews' wird von manchen Newsreadern zum Senden von
Nachrichten verwendet. Es führt eine Konsistenzprüfung und Header-Neuf
ormatierung aus und leitet die Nachricht an den in 'inn.conf'
angegebenen News-Server weiter.

%description -n inews -l es
El programa inews se usa por algunos lectores de news para postar
mensajes. Hace alguna consistencia chequeando y reformateando headers,
y enviando el artículo para el servidor de news especificado en el
inn.conf.

%description -n inews -l fr
Le programme inews est utilisé par certains lecteurs de news pour
poster les articles. Il effectue des vérifications et un reformatage
des en-têtes et fait suivre l'article au serveur de news spécifié dans
inn.conf.

%description -n inews -l pl
Inews jest u¿ywany przez niektóre czytniki news do wysy³ania
artyku³ów. Sprawdza budowê artyku³u, przepisuje nag³ówek i wysy³a do
serwera news wyszczególnionego w inn.conf.

%description -n inews -l pt_BR
O programa inews é usado por alguns leitores de news para postar
mensagens. Ele faz alguma consistência checando e reformatando
headers, e enviando o artigo para o servidor de news especificado no
inn.conf.

%description -n inews -l tr
inews programý bazý haber okuyucular tarafýndan haber yollamak
amacýyla kullanýlýr. Program bazý güvenlik denetimleri ve baþlýk
biçimlendirmesi yaparak ve inn.conf dosyasýnda belirtilen haber
sunucuya makaleyi yollar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch11 -p1	-- obsolete? (no setreuid test)
#%patch12 -p1	-- obsolete? (pathrun not used in inndstart)
#%patch13 -p1	-- obsolete? (?)

touch innfeed/*.[ly]

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE" \
	--with-news-user=news \
	--with-news-group=news \
	--with-news-master=news \
	--with-db-dir=/var/lib/news \
	--with-etc-dir=%{_sysconfdir} \
	--with-log-dir=/var/log/news \
	--with-run-dir=/var/run/news \
	--with-spool-dir=/var/spool/news \
	--with-lib-dir=%{_datadir}/news \
	--with-tmp-path=/var/spool/news/incoming/tmp \
	--with-perl \
	--with-sendmail=%{_libdir}/sendmail \
	--with-openssl=%{_prefix} \
	--with-berkeleydb=%{_prefix} \
	%{?_with_largefiles:--enable-largefiles} \
	%{!?_with_largefiles:--enable-tagged-hash} \
	--enable-merge-to-groups \
	--enable-pgp-verify \
	--enable-shared \
	--enable-static \
	--enable-libtool \
	--enable-ipv6 \
	--enable-dual-socket

%{__make} all \
	PATHFILTER=%{_datadir}/news/filter \
	PATHCONTROL=%{_datadir}/news/control

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{news,rc.d/init.d,cron.d,logrotate.d} \
	$RPM_BUILD_ROOT{%{_libdir}/news/{rnews,auth/generic},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/news/{control,filter,auth}} \
	$RPM_BUILD_ROOT%{_mandir}/{man{1,3,5,8},pl/man{1,8}} \
	$RPM_BUILD_ROOT/var/{run/news,lib/news/backoff,log/{news,archiv/news}} \
	$RPM_BUILD_ROOT/var/spool/news/{articles,overview,incoming/{tmp,bad},outgoing,archive,uniover,innfeed,cycbuffs} \
	$RPM_BUILD_ROOT/home/services/news

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	PATHFILTER=%{_datadir}/news/filter \
	PATHCONTROL=%{_datadir}/news/control \
	PATHRNEWS=%{_libdir}/news/rnews \
	PATHAUTHPASSWD=%{_libdir}/news/auth/passwd \
	PATHAUTHRESOLV=%{_libdir}/news/auth/resolv

install samples/readers.conf $RPM_BUILD_ROOT%{_sysconfdir}/readers.conf

install %{SOURCE1} $RPM_BUILD_ROOT/var/lib/news/active
install %{SOURCE2} $RPM_BUILD_ROOT/var/lib/news/distributions
install %{SOURCE3} $RPM_BUILD_ROOT/var/lib/news/newsgroups
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/inn.conf
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/newsfeeds
install %{SOURCE6} $RPM_BUILD_ROOT/etc/cron.d/inn
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/inn
install %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/cnfsstat.cron
install %{SOURCE9} $RPM_BUILD_ROOT/etc/logrotate.d/inn
install %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/readers.conf
install %{SOURCE11} $RPM_BUILD_ROOT%{_mandir}/pl/man1/getlist.1
install %{SOURCE12} $RPM_BUILD_ROOT%{_mandir}/pl/man8/innd.8

rm -f $RPM_BUILD_ROOT/var/lib/news/history

umask 002
> $RPM_BUILD_ROOT%{_sysconfdir}/subscriptions
touch $RPM_BUILD_ROOT/var/lib/news/history
touch $RPM_BUILD_ROOT/var/lib/news/.news.daily
touch $RPM_BUILD_ROOT/var/lib/news/active.times
touch $RPM_BUILD_ROOT/var/log/news/news.notice
touch $RPM_BUILD_ROOT/var/log/news/news.crit
touch $RPM_BUILD_ROOT/var/log/news/news.err

# obsolete?
#touch $RPM_BUILD_ROOT%{_includedir}/inn/configdata.h

mv -f $RPM_BUILD_ROOT%{_datadir}/news/*.{a,la,so*} $RPM_BUILD_ROOT%{_libdir}

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_bindir}/makehistory \
	-a $RPM_BUILD_ROOT/var/lib/news/active \
	-i -r -f $RPM_BUILD_ROOT/var/lib/news/history || :

#Fix perms in sample directory to avoid bogus dependencies
find samples -name "*.in" -exec chmod a-x {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "`getent passwd http | cut -d: -f6`" = "/var/spool/news" ]; then
	/usr/sbin/usermod -d /home/services/news news
fi
umask 022
if [ -f /var/lib/news/history ]; then
	cd /var/lib/news
	%{_bindir}/makedbz -s `wc -l <history` -f history
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news:news history.*
	chmod 644 history.*
else
	cd /var/lib/news
	cp /dev/null history
	%{_bindir}/makehistory
	%{_bindir}/makedbz -s `wc -l <history` -f history
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news:news history history.*
	chmod 644 history history.*
fi
[ -f /var/lib/news/active.times ] || {
	touch /var/lib/news/active.times
	chown news:news /var/lib/news/active.times
}

[ -f /var/log/news/news.notice ] || {
	touch /var/log/news/news.notice
	chown news:news /var/log/news/news.notice
	chmod 664 /var/log/news/news.notice
}

[ -f /var/log/news/news.crit ] || {
	touch /var/log/news/news.crit
	chown news:news /var/log/news/news.crit
	chmod 660 /var/log/news/news.crit
}

[ -f /var/log/news/news.err ] || {
	touch /var/log/news/news.err
	chown news:news /var/log/news/news.err
	chmod 660 /var/log/news/news.err
}

[ -f /var/lib/news/.news.daily ] || {
	touch /var/lib/news/.news.daily
	chown news:news /var/lib/news/.news.daily
	chmod 664 /var/lib/news/.news.daily
}

umask 027
if [ -f /etc/syslog.conf ]; then
  if ! grep -q INN /etc/syslog.conf; then
    sed 's/mail.none;/mail.none;news.none;/' < /etc/syslog.conf > /etc/syslog.conf.inn
    mv -f /etc/syslog.conf.inn /etc/syslog.conf
    echo ''										>> /etc/syslog.conf
    echo '#'										>> /etc/syslog.conf
    echo '# INN'									>> /etc/syslog.conf
    echo '#' 										>> /etc/syslog.conf
    echo 'news.=crit                                        /var/log/news/news.crit'	>> /etc/syslog.conf
    echo 'news.=err                                         /var/log/news/news.err'	>> /etc/syslog.conf
    echo 'news.notice                                       /var/log/news/news.notice'	>> /etc/syslog.conf
    fi
  if [ -f /var/run/syslog.pid ]; then
    kill -HUP `cat /var/run/syslog.pid` 2> /dev/null ||:
  fi
else
    # syslog.conf does not exist
    echo "mail.none /var/log/messages" 							> /etc/syslog.conf.inn
    echo "" 										>> /etc/syslog.conf.inn
    echo "# INN" 									>> /etc/syslog.conf.inn
    echo "news.=crit                                      /var/log/news/news.crit"	>> /etc/syslog.conf.inn
    echo "news.=err                                       /var/log/news/news.err"	>> /etc/syslog.conf.inn
    echo "news.notice                                     /var/log/news/news.notice"	>> /etc/syslog.conf.inn
fi

/sbin/chkconfig --add inn
if [ -f /var/lock/subsys/inn ]; then
	/etc/rc.d/init.d/inn restart >&2
else
	echo "Run \"/etc/rc.d/init.d/inn start\" to start inn news server." >&2
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/news ]; then
		/etc/rc.d/init.d/inn stop
	fi
	/sbin/chkconfig --del inn
fi

%triggerpostun -- inn < 2.4.0
cp -af %{_sysconfdir}/inn.conf{,.rpmorig}
sed -e 's/^\(listenonipv6\)/#\1/;s/^bindipv6address/bindaddress6/;s/^sourceipv6address/sourceaddress6/' \
	%{_sysconfdir}/inn.conf.rpmorig > %{_sysconfdir}/inn.conf

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS ChangeLog INSTALL LICENSE NEWS README TODO doc/[Icehs]*

# DB
%attr(770,root,news) %dir /var/lib/news
%attr(770,root,news) %dir /var/lib/news/backoff
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/active
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/distributions
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/newsgroups
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/active.times
%attr(664,news,news) %ghost /var/lib/news/.news.daily
%attr(664,news,news) %ghost /var/lib/news/history

# LOGS
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/logrotate.d/inn
%attr(770,root,news) %dir /var/log/news
%attr(770,root,news) %dir /var/log/archiv/news
%attr(770,news,news) %dir /var/run/news
%attr(664,news,news) %ghost /var/log/news/news.notice
%attr(660,news,news) %ghost /var/log/news/news.crit
%attr(660,news,news) %ghost /var/log/news/news.err

# SPOOL
%attr(771,root,news) %dir /var/spool/news
%attr(770,root,news) %dir /var/spool/news/archive
%attr(770,root,news) %dir /var/spool/news/articles
%attr(770,root,news) %dir /var/spool/news/cycbuffs
%attr(770,root,news) %dir /var/spool/news/incoming
%attr(770,root,news) %dir /var/spool/news/incoming/bad
%attr(770,root,news) %dir /var/spool/news/incoming/tmp
%attr(770,root,news) %dir /var/spool/news/innfeed
%attr(770,root,news) %dir /var/spool/news/outgoing
%attr(770,root,news) %dir /var/spool/news/overview
%attr(770,root,news) %dir /var/spool/news/uniover

# CRON PARTS
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/cron.d/inn

# RC-SCRIPT
%attr(754,root,root) /etc/rc.d/init.d/inn

# CONFIGS (INN is a one big config ;-)
%attr(755,root,news) %dir %{_sysconfdir}
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/actsync.cfg
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/actsync.ign
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/buffindexed.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/control.ctl
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cycbuff.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/distrib.pats
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/expire.ctl
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/incoming.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/inn.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/innfeed.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/innreport.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/innwatch.ctl
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/moderators
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/motd.news
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/news2mail.cf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/newsfeeds
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nnrpd.track
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nntpsend.ctl
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ovdb.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/overview.fmt
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/passwd.nntp
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/radius.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/readers.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/sasl.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/storage.conf
%attr(640,root,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/subscriptions

%attr(755,root,news) %dir %{_datadir}/news
%attr(755,root,root) %dir %{_datadir}/news/control
%attr(755,root,root) %dir %{_datadir}/news/filter

%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/innreport_inn.pm
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/innshellvars
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/innshellvars.pl
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/innshellvars.tcl

%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/filter/INN.py
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/filter/filter_nnrpd.pl
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/filter/filter.tcl
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/filter/nnrpd_auth.pl
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/filter/nnrpd_auth.py
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/filter/startup_innd.pl
%config(noreplace) %verify(not size mtime md5) %{_datadir}/news/filter/startup.tcl

%attr(755,root,root) %{_datadir}/news/control/checkgroups.pl
%attr(755,root,root) %{_datadir}/news/control/ihave.pl
%attr(755,root,root) %{_datadir}/news/control/newgroup.pl
%attr(755,root,root) %{_datadir}/news/control/rmgroup.pl
%attr(755,root,root) %{_datadir}/news/control/sendme.pl
%attr(755,root,root) %{_datadir}/news/control/sendsys.pl
%attr(755,root,root) %{_datadir}/news/control/senduuname.pl
%attr(755,root,root) %{_datadir}/news/control/version.pl

%attr(755,root,news) %dir %{_libdir}/news
%attr(755,root,root) %dir %{_libdir}/news/auth
%attr(755,root,root) %dir %{_libdir}/news/auth/generic
%attr(755,root,root) %dir %{_libdir}/news/auth/passwd
%attr(755,root,root) %dir %{_libdir}/news/auth/resolv
%attr(755,root,root) %dir %{_libdir}/news/rnews

%attr(755,root,root) %{_libdir}/news/auth/passwd/*
%attr(755,root,root) %{_libdir}/news/auth/resolv/*
%attr(755,root,root) %{_libdir}/news/rnews/*

# SUID
%attr(4754,root,news) %{_bindir}/inndstart
%attr(4754,root,news) %{_bindir}/startinnfeed
%attr(4754,root,news) %{_bindir}/rnews

# BINARIES
%attr(755,root,root) %{_bindir}/actmerge
%attr(755,root,root) %{_bindir}/actsync
%attr(755,root,root) %{_bindir}/actsyncd
%attr(755,root,root) %{_bindir}/archive
%attr(755,root,root) %{_bindir}/batcher
%attr(755,root,root) %{_bindir}/buffchan
%attr(755,root,root) %{_bindir}/cnfsheadconf
%attr(755,root,root) %{_bindir}/cnfsstat
%attr(755,root,root) %{_bindir}/cnfsstat.cron
%attr(755,root,root) %{_bindir}/controlbatch
%attr(755,root,root) %{_bindir}/controlchan
%attr(755,root,root) %{_bindir}/convdate
%attr(755,root,root) %{_bindir}/ctlinnd
%attr(755,root,root) %{_bindir}/cvtbatch
%attr(755,root,root) %{_bindir}/docheckgroups
%attr(755,root,root) %{_bindir}/expire
%attr(755,root,root) %{_bindir}/expireover
%attr(755,root,root) %{_bindir}/expirerm
%attr(755,root,root) %{_bindir}/fastrm
%attr(755,root,root) %{_bindir}/filechan
%attr(755,root,root) %{_bindir}/getlist
%attr(755,root,root) %{_bindir}/gpgverify
%attr(755,root,root) %{_bindir}/grephistory
%attr(755,root,root) %{_bindir}/imapfeed
%attr(755,root,root) %{_bindir}/inncheck
%attr(755,root,root) %{_bindir}/innconfval
%attr(755,root,root) %{_bindir}/innd
%attr(755,root,root) %{_bindir}/inndf
%attr(755,root,root) %{_bindir}/innfeed
%attr(755,root,root) %{_bindir}/innmail
%attr(755,root,root) %{_bindir}/innreport
%attr(755,root,root) %{_bindir}/innstat
%attr(755,root,root) %{_bindir}/innupgrade
%attr(755,root,root) %{_bindir}/innwatch
%attr(755,root,root) %{_bindir}/innxbatch
%attr(755,root,root) %{_bindir}/innxmit
%attr(755,root,root) %{_bindir}/mailpost
%attr(755,root,root) %{_bindir}/makedbz
%attr(755,root,root) %{_bindir}/makehistory
%attr(755,root,root) %{_bindir}/mod-active
%attr(755,root,root) %{_bindir}/news.daily
%attr(755,root,root) %{_bindir}/news2mail
%attr(755,root,root) %{_bindir}/ninpaths
%attr(755,root,root) %{_bindir}/nnrpd
%attr(755,root,root) %{_bindir}/nntpget
%attr(755,root,root) %{_bindir}/nntpsend
%attr(755,root,root) %{_bindir}/ovdb_*
%attr(755,root,root) %{_bindir}/overchan
%attr(755,root,root) %{_bindir}/perl-nocem
%attr(755,root,root) %{_bindir}/pgpverify
%attr(755,root,root) %{_bindir}/procbatch
%attr(755,root,root) %{_bindir}/prunehistory
%attr(755,root,root) %{_bindir}/pullnews
%attr(755,root,root) %{_bindir}/scanlogs
%attr(755,root,root) %{_bindir}/scanspool
%attr(755,root,root) %{_bindir}/send-ihave
%attr(755,root,root) %{_bindir}/send-nntp
%attr(755,root,root) %{_bindir}/send-uucp
%attr(755,root,root) %{_bindir}/sendinpaths
%attr(755,root,root) %{_bindir}/sendxbatches
%attr(755,root,root) %{_bindir}/shlock
%attr(755,root,root) %{_bindir}/shrinkfile
%attr(755,root,root) %{_bindir}/signcontrol
%attr(755,root,root) %{_bindir}/simpleftp
%attr(755,root,root) %{_bindir}/sm
%attr(755,root,root) %{_bindir}/tally.control
%attr(755,root,root) %{_bindir}/tdx-util
%attr(755,root,root) %{_bindir}/writelog

# MAN
%{_mandir}/man1/convdate.1*
%{_mandir}/man1/fastrm.1*
%{_mandir}/man1/getlist.1*
%{_mandir}/man1/grephistory.1*
%{_mandir}/man1/innconfval.1*
%{_mandir}/man1/innfeed.1*
%{_mandir}/man1/innmail.1*
%{_mandir}/man1/nntpget.1*
%{_mandir}/man1/pgpverify.1*
%{_mandir}/man1/rnews.1*
%{_mandir}/man1/shlock.1*
%{_mandir}/man1/shrinkfile.1*
%{_mandir}/man1/simpleftp.1*
%{_mandir}/man1/sm.1*
%{_mandir}/man1/startinnfeed.1*
%{_mandir}/man[58]/*
%lang(pl) %{_mandir}/pl/man1/getlist.1*
%lang(pl) %{_mandir}/pl/man8/innd.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n inews
%defattr(644,root,root,755)
%attr(755,root,news) %{_bindir}/inews
%{_mandir}/man1/inews.1*
