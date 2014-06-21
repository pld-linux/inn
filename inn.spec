#
# Conditional build:
%bcond_with	largefiles	# enable largefiles (disables tagged hash)

%include	/usr/lib/rpm/macros.perl
Summary:	INN, the InterNet News System (news server)
Summary(de.UTF-8):	das InterNet News System (News-Server)
Summary(es.UTF-8):	INN, InterNet News System (servidor news)
Summary(fr.UTF-8):	INN, le système InterNet News (serveur de news)
Summary(pl.UTF-8):	INN, serwer nowinek
Summary(pt_BR.UTF-8):	INN, InterNet News System (servidor news)
Summary(tr.UTF-8):	INN, InterNet Haber Sistemi (haber sunucu)
Name:		inn
Version:	2.5.4
Release:	1
License:	distributable
Group:		Networking/Daemons
Source0:	ftp://ftp.isc.org/isc/inn/%{name}-%{version}.tar.gz
# Source0-md5:	ad9f77a1c84c668ccd268792721a2215
Source1:	%{name}-default-active
Source2:	%{name}-default-distributions
Source3:	%{name}-default-newsgroups
Source4:	%{name}.crontab
Source5:	%{name}.init
Source6:	%{name}-cnfsstat.cron
Source7:	%{name}.logrotate
Source8:	getlist.1.pl
Source9:	%{name}d.8.pl
Source10:	%{name}.tmpfiles
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-install.patch
Patch3:		%{name}-setgid.patch
Patch4:		%{name}-config.patch
Patch5:		%{name}-asneeded.patch
Patch6:		%{name}-nnrpd_no_trace.patch
Patch8:		%{name}-libdir.patch
URL:		https://www.isc.org/software/inn/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	db-devel >= 4.4
BuildRequires:	flex >= 2.5.37
BuildRequires:	heimdal-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.663
Requires(post):	/bin/kill
Requires(post):	/usr/bin/getent
Requires(post):	/usr/sbin/usermod
Requires(post):	fileutils
Requires(post):	sed >= 4.0
Requires(post):	textutils
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	awk
Requires:	cleanfeed >= 0.95.7b-4
Requires:	crondaemon
Requires:	procps
Requires:	psmisc >= 20.1
Requires:	rc-scripts >= 0.4.1.23
Requires:	textutils
Requires:	util-linux
Suggests:	perl-GD
Provides:	nntpserver
Obsoletes:	leafnode
Obsoletes:	leafnode+
Conflicts:	logrotate < 3.7-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/news
%define		_includedir	%{_prefix}/include/inn

%define		skip_post_check_so	libstorage.so.*
# /usr/bin/pullnews doesn't provide perl(Net::NNTP) - perl-libnet does.
%define		_noautoprov_perl	Net::NNTP
# it's necessary only for sample nnrpd_auth.pl hook
%define		_noautoreq_perl		CDB_File

%description
INN is a news server, which can be set up to handle USENET news, as
well as private "newsfeeds". There is a *LOT* of information about
setting up INN in %{_docdir}/%{name}-%{version} -- read it.

If you want innreport to generate graphs you need perl-GD package.

%description -l es.UTF-8
INN es un servidor de news, que puede ser configurado para manipular
USENET news bien como newsfeeds privadas. Existe un *Montón* de
información sobre la configuración del INN en
%{_docdir}/%{name}-%{version} -- léela.

%description -l pl.UTF-8
INN jest serwerem news, który można skonfigurować do obsługi USENET-u,
jak również do obsługi ,,prywatnych'' grup w sieciach intranetowych.
Całe mnóstwo pożytecznych informacji o konfigurowaniu INN-a znajdziesz
w katalogu %{_docdir}/%{name}-%{version}.

Aby innreport generował wykresy, trzeba zainstalować pakiet perl-GD.

%description -l pt_BR.UTF-8
INN é um servidor de news, que pode ser configurado para manipular
USENET news bem como newsfeeds privadas. Existe um *MONTE* de
informações sobre a configuração do INN em
%{_docdir}/%{name}-%{version} -- leia.

%package libs
Summary:	INN libraries
Summary(de.UTF-8):	INN-Library
Summary(fr.UTF-8):	Bibliothèque INN
Summary(pl.UTF-8):	Biblioteki do INN-a
Group:		Libraries

%description libs
This library is needed by several programs that interface to INN, such
as newsgate or tin.

%description libs -l de.UTF-8
Diese Library wird von mehreren Programmen benötigt, die mit INN
kommunizieren, etwa newsgate oder tin.

%description libs -l fr.UTF-8
Cette bibliothèque est nécessaire à plusieurs programmes qui
s'interfacent avec INN, comme newsgate ou tin.

%description libs -l pl.UTF-8
Biblioteka niezbędna do działania kilku programów współpracujących z
INN-em, takich jak newsgate czy tin.

%description libs -l tr.UTF-8
INN ile arayüz gerektiren programlar için (newsgate, tin gibi) gereken
bir kitaplıktır.

%package devel
Summary:	INN header files and development documentations
Summary(de.UTF-8):	INN-Library
Summary(es.UTF-8):	Biblioteca INN
Summary(fr.UTF-8):	Bibliothèque INN
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programisty do inn-a
Summary(pt_BR.UTF-8):	Biblioteca INN
Summary(tr.UTF-8):	INN kitaplığı
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	db-devel

%description devel
Header files and developer documentations for INN libraries.

%description devel -l de.UTF-8
Diese Library wird von mehreren Programmen benötigt, die mit INN
kommunizieren, etwa newsgate oder tin.

%description devel -l es.UTF-8
Esta biblioteca es requerida por varios programas que tienen interface
con INN, como el newsgate o tin.

%description devel -l fr.UTF-8
Cette bibliothèque est nécessaire à plusieurs programmes qui
s'interfacent avec INN, comme newsgate ou tin.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do bibliotek INN-a.

%description devel -l pt_BR.UTF-8
Esta biblioteca é requerida por vários programas que tem interface com
o INN, como o newsgate ou tin.

%description devel -l tr.UTF-8
INN ile arayüz gerektiren programlar için (newsgate, tin gibi) gereken
bir kitaplıktır.

%package static
Summary:	Static INN libraries
Summary(es.UTF-8):	Static libraries for inn development
Summary(pl.UTF-8):	Biblioteki statyczne do INN
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com inn
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static INN libraries.

%description static -l es.UTF-8
Static libraries for inn development

%description static -l pl.UTF-8
Biblioteki statyczne do INN.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com inn

%package -n inews
Summary:	Inews program (used for posting by inn and trn)
Summary(de.UTF-8):	Inews-Programm (für die Zustellung mit inn und trn)
Summary(es.UTF-8):	Programa Inews (usado para franqueo por inn y trn)
Summary(fr.UTF-8):	Programme inews (utilisé par inn et trn pour poster)
Summary(pl.UTF-8):	Inews - program do wysyłania artykułów (używany przez inn i trn)
Summary(pt_BR.UTF-8):	Programa Inews (usado para postagem pelo inn e trn)
Summary(tr.UTF-8):	Haber biçimlendirme programı
Group:		Networking/News
Requires:	%{name}-libs = %{version}-%{release}

%description -n inews
The inews program is used by some news readers to post news. It does
some consistency checking and header reformatting, and forwards the
article on to the news server specified in inn.conf.

%description -n inews -l de.UTF-8
Das Programm 'inews' wird von manchen Newsreadern zum Senden von
Nachrichten verwendet. Es führt eine Konsistenzprüfung und Header-Neuf
ormatierung aus und leitet die Nachricht an den in 'inn.conf'
angegebenen News-Server weiter.

%description -n inews -l es.UTF-8
El programa inews se usa por algunos lectores de news para postar
mensajes. Hace alguna consistencia chequeando y reformateando headers,
y enviando el artículo para el servidor de news especificado en el
inn.conf.

%description -n inews -l fr.UTF-8
Le programme inews est utilisé par certains lecteurs de news pour
poster les articles. Il effectue des vérifications et un reformatage
des en-têtes et fait suivre l'article au serveur de news spécifié dans
inn.conf.

%description -n inews -l pl.UTF-8
Inews jest używany przez niektóre czytniki news do wysyłania
artykułów. Sprawdza budowę artykułu, przepisuje nagłówek i wysyła do
serwera news wyszczególnionego w inn.conf.

%description -n inews -l pt_BR.UTF-8
O programa inews é usado por alguns leitores de news para postar
mensagens. Ele faz alguma consistência checando e reformatando
headers, e enviando o artigo para o servidor de news especificado no
inn.conf.

%description -n inews -l tr.UTF-8
inews programı bazı haber okuyucular tarafından haber yollamak
amacıyla kullanılır. Program bazı güvenlik denetimleri ve başlık
biçimlendirmesi yaparak ve inn.conf dosyasında belirtilen haber
sunucuya makaleyi yollar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1

touch innfeed/*.[ly]

%build
%{__libtoolize}
# not updated automatically by libtool
cp -f /usr/share/aclocal/{libtool,lt*}.m4 m4
cp -f /usr/share/automake/config.* support
%{__aclocal}
%{__autoconf}
%{__autoheader} -I include
%configure \
	CPPFLAGS="-D_GNU_SOURCE" \
	--with-news-group=news \
	--with-news-master=news \
	--with-news-user=news \
	--with-control-dir=%{_datadir}/news/control \
	--with-db-dir=/var/lib/news \
	--with-filter-dir=%{_datadir}/news/filter \
	--with-http-dir=%{_datadir}/news/http \
	--with-innlib-dir=%{_datadir}/news \
	--with-libperl-dir=%{perl_vendorlib} \
	--with-log-dir=/var/log/news \
	--with-run-dir=/var/run/news \
	--with-spool-dir=/var/spool/news \
	--with-tmp-dir=/var/spool/news/incoming/tmp \
	--with-berkeleydb=%{_prefix} \
	--with-openssl=%{_prefix} \
	--with-perl \
	--with-sendmail=/usr/lib/sendmail \
	--enable-ipv6 \
	%{?with_largefiles:--enable-largefiles} \
	--enable-libtool \
	--enable-shared \
	--enable-static \
	%{!?with_largefiles:--enable-tagged-hash}

%{__make} all \
	PATHFILTER=%{_datadir}/news/filter \
	PATHCONTROL=%{_datadir}/news/control

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{news/pgp,rc.d/init.d,cron.d,logrotate.d} \
	$RPM_BUILD_ROOT{%{_libdir}/news/{rnews,auth/generic},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/news/{control,filter,auth}} \
	$RPM_BUILD_ROOT%{_mandir}/{man{1,3,5,8},pl/man{1,8}} \
	$RPM_BUILD_ROOT/var/{run/news,lib/news/backoff,log/{news,archive/news}} \
	$RPM_BUILD_ROOT/var/spool/news/{articles,overview,incoming/{tmp,bad},outgoing,archive,uniover,innfeed,cycbuffs} \
	$RPM_BUILD_ROOT/home/services/news \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BACKUP_OPTION= \
	PATHFILTER=%{_datadir}/news/filter \
	PATHCONTROL=%{_datadir}/news/control \
	PATHRNEWS=%{_libdir}/news/rnews \
	PATHAUTHPASSWD=%{_libdir}/news/auth/passwd \
	PATHAUTHRESOLV=%{_libdir}/news/auth/resolv

cp -p samples/readers.conf $RPM_BUILD_ROOT%{_sysconfdir}/readers.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/motd.{innd,nnrpd}

cp -p %{SOURCE1} $RPM_BUILD_ROOT/var/lib/news/active
cp -p %{SOURCE2} $RPM_BUILD_ROOT/var/lib/news/distributions
cp -p %{SOURCE3} $RPM_BUILD_ROOT/var/lib/news/newsgroups
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.d/inn
install -p %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/inn
install -p %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/cnfsstat.cron
cp -p %{SOURCE7} $RPM_BUILD_ROOT/etc/logrotate.d/inn
cp -p %{SOURCE8} $RPM_BUILD_ROOT%{_mandir}/pl/man1/getlist.1
cp -p %{SOURCE9} $RPM_BUILD_ROOT%{_mandir}/pl/man8/innd.8
cp -p %{SOURCE10} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

%{__rm} $RPM_BUILD_ROOT/var/lib/news/history

umask 002
:> $RPM_BUILD_ROOT%{_sysconfdir}/subscriptions
touch $RPM_BUILD_ROOT/var/lib/news/.news.daily
touch $RPM_BUILD_ROOT/var/lib/news/active.times
touch $RPM_BUILD_ROOT/var/lib/news/history

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_bindir}/makehistory \
	-a $RPM_BUILD_ROOT/var/lib/news/active \
	-r -f $RPM_BUILD_ROOT/var/lib/news/history || :

# Fix perms in sample directory to avoid bogus dependencies
find samples -name "*.in" -exec chmod a-x {} \;

# remove files in conflict with cleanfeed
%{__rm} $RPM_BUILD_ROOT%{_datadir}/news/filter/filter_innd.*

# remove unpackaged files
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc
%{__rm} $RPM_BUILD_ROOT%{_bindir}/rc.news

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "`getent passwd news | cut -d: -f6`" = "/var/spool/news" ]; then
	/usr/sbin/usermod -d /home/services/news news
fi

umask 022

%{_bindir}/innupgrade %{_sysconfdir}

cd /var/lib/news
if [ ! -f /var/lib/news/history ]; then
	# makehistory fails on uninitialized spool(?) - create empty history in such case
	%{_bindir}/makehistory || { echo "Creating empty history"; :> history; }
	chown news:news history
	chmod 664 history
	%{_bindir}/makedbz -s `wc -l < history` -f history
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news:news history.*
	chmod 644 history.*
fi

if [ ! -f /var/lib/news/.news.daily ]; then
	:> /var/lib/news/.news.daily
	chown news:news /var/lib/news/.news.daily
	chmod 664 /var/lib/news/.news.daily
fi

/sbin/chkconfig --add inn
%service inn restart "inn news server"

%preun
if [ "$1" = "0" ]; then
	%service inn stop
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
%attr(700,news,news) %dir /home/services/news

# DB
%attr(770,root,news) %dir /var/lib/news
%attr(770,root,news) %dir /var/lib/news/backoff
%attr(664,root,news) %config(noreplace) %verify(not md5 mtime size) /var/lib/news/active
%attr(664,root,news) %config(noreplace) %verify(not md5 mtime size) /var/lib/news/active.times
%attr(664,root,news) %config(noreplace) %verify(not md5 mtime size) /var/lib/news/distributions
%attr(664,root,news) %config(noreplace) %verify(not md5 mtime size) /var/lib/news/newsgroups
%attr(664,news,news) %ghost /var/lib/news/.news.daily
%attr(664,news,news) %ghost /var/lib/news/history

# LOGS
%{systemdtmpfilesdir}/%{name}.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/inn
# note: innd (and maybe others) creates files in this directory
%attr(771,root,news) %dir /var/log/news
%attr(770,news,news) %dir /var/run/news

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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/inn

# RC-SCRIPT
%attr(754,root,root) /etc/rc.d/init.d/inn

# CONFIGS (INN is a one big config ;-)
%attr(755,root,news) %dir %{_sysconfdir}
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/actsync.cfg
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/actsync.ign
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/buffindexed.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/control.ctl
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/control.ctl.local
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/cycbuff.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/distrib.pats
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/distributions
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/expire.ctl
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/incoming.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/inn.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/inn-radius.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/innfeed.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/innreport.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/innshellvars.local
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/innshellvars.pl.local
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/innshellvars.tcl.local
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/innwatch.ctl
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/localgroups
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/moderators
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/motd.innd
%{_sysconfdir}/motd.innd.sample
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/motd.nnrpd
%{_sysconfdir}/motd.nnrpd.sample
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/news2mail.cf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/newsfeeds
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nnrpd.track
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nntpsend.ctl
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/nocem.ctl
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ovdb.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/passwd.nntp
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/readers.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/send-uucp.cf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/storage.conf
%attr(640,root,news) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/subscriptions
%attr(755,root,news) %dir %{_sysconfdir}/pgp

%attr(755,root,news) %dir %{_datadir}/news
%dir %{_datadir}/news/control
%dir %{_datadir}/news/filter
%dir %{_datadir}/news/http
%{_datadir}/news/http/innreport.css

%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/innreport_inn.pm
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/innshellvars
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/innshellvars.pl
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/innshellvars.tcl

%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/INN.py
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/filter_nnrpd.pl
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/nnrpd.py
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/nnrpd_access.pl
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/nnrpd_access.py
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/nnrpd_auth.pl
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/nnrpd_auth.py
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/nnrpd_dynamic.py
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/news/filter/startup_innd.pl

%attr(755,root,root) %{_datadir}/news/control/checkgroups.pl
%attr(755,root,root) %{_datadir}/news/control/ihave.pl
%attr(755,root,root) %{_datadir}/news/control/newgroup.pl
%attr(755,root,root) %{_datadir}/news/control/rmgroup.pl
%attr(755,root,root) %{_datadir}/news/control/sendme.pl
%attr(755,root,root) %{_datadir}/news/control/sendsys.pl
%attr(755,root,root) %{_datadir}/news/control/senduuname.pl
%attr(755,root,root) %{_datadir}/news/control/version.pl

%dir %{perl_vendorlib}/INN
%{perl_vendorlib}/INN/Config.pm
%dir %{perl_vendorlib}/INN/Utils
%{perl_vendorlib}/INN/Utils/Shlock.pm

%attr(755,root,news) %dir %{_libdir}/news
%dir %{_libdir}/news/auth
%dir %{_libdir}/news/auth/generic
%dir %{_libdir}/news/auth/passwd
%dir %{_libdir}/news/auth/resolv
%dir %{_libdir}/news/rnews

%attr(755,root,root) %{_libdir}/news/auth/passwd/*
%attr(755,root,root) %{_libdir}/news/auth/resolv/*
%attr(755,root,root) %{_libdir}/news/rnews/*

# BINARIES
%attr(755,root,root) %{_bindir}/actmerge
%attr(755,root,root) %{_bindir}/actsync
%attr(755,root,root) %{_bindir}/actsyncd
%attr(755,root,root) %{_bindir}/archive
%attr(755,root,root) %{_bindir}/batcher
%attr(755,root,root) %{_bindir}/buffchan
%attr(755,root,root) %{_bindir}/buffindexed_d
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
%attr(755,root,root) %{_bindir}/grephistory
%attr(755,root,root) %{_bindir}/imapfeed
# suid root to bind sockets
%attr(4754,root,news) %{_bindir}/innbind
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
%attr(755,root,root) %{_bindir}/rnews
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
%attr(755,root,root) %{_bindir}/tinyleaf
%attr(755,root,root) %{_bindir}/writelog

# MAN
%{_mandir}/man1/convdate.1*
%{_mandir}/man1/fastrm.1*
%{_mandir}/man1/getlist.1*
%{_mandir}/man1/grephistory.1*
%{_mandir}/man1/innconfval.1*
%{_mandir}/man1/innmail.1*
%{_mandir}/man1/nntpget.1*
%{_mandir}/man1/pgpverify.1*
%{_mandir}/man1/pullnews.1*
%{_mandir}/man1/rnews.1*
%{_mandir}/man1/shlock.1*
%{_mandir}/man1/shrinkfile.1*
%{_mandir}/man1/simpleftp.1*
%{_mandir}/man1/sm.1*
%{_mandir}/man3/INN::Config.3pm*
%{_mandir}/man3/INN::Utils::Shlock.3pm*
%{_mandir}/man5/active.5*
%{_mandir}/man5/active.times.5*
%{_mandir}/man5/buffindexed.conf.5*
%{_mandir}/man5/control.ctl.5*
%{_mandir}/man5/cycbuff.conf.5*
%{_mandir}/man5/distrib.pats.5*
%{_mandir}/man5/distributions.5*
%{_mandir}/man5/expire.ctl.5*
%{_mandir}/man5/history.5*
%{_mandir}/man5/incoming.conf.5*
%{_mandir}/man5/inn.conf.5*
%{_mandir}/man5/inn-radius.conf.5*
%{_mandir}/man5/innfeed.conf.5*
%{_mandir}/man5/innwatch.ctl.5*
%{_mandir}/man5/localgroups.5*
%{_mandir}/man5/moderators.5*
%{_mandir}/man5/motd.innd.5*
%{_mandir}/man5/motd.news.5*
%{_mandir}/man5/motd.nnrpd.5*
%{_mandir}/man5/newsfeeds.5*
%{_mandir}/man5/newsgroups.5*
%{_mandir}/man5/newslog.5*
%{_mandir}/man5/nnrpd.track.5*
%{_mandir}/man5/nntpsend.ctl.5*
%{_mandir}/man5/nocem.ctl.5*
%{_mandir}/man5/ovdb.5*
%{_mandir}/man5/passwd.nntp.5*
%{_mandir}/man5/readers.conf.5*
%{_mandir}/man5/storage.conf.5*
%{_mandir}/man5/subscriptions.5*
%{_mandir}/man8/actsync.8*
%{_mandir}/man8/actsyncd.8*
%{_mandir}/man8/archive.8*
%{_mandir}/man8/batcher.8*
%{_mandir}/man8/buffchan.8*
%{_mandir}/man8/ckpasswd.8*
%{_mandir}/man8/cnfsheadconf.8*
%{_mandir}/man8/cnfsstat.8*
%{_mandir}/man8/controlchan.8*
%{_mandir}/man8/ctlinnd.8*
%{_mandir}/man8/cvtbatch.8*
%{_mandir}/man8/docheckgroups.8*
%{_mandir}/man8/domain.8*
%{_mandir}/man8/expire.8*
%{_mandir}/man8/expireover.8*
%{_mandir}/man8/expirerm.8*
%{_mandir}/man8/filechan.8*
%{_mandir}/man8/ident.8*
%{_mandir}/man8/imapfeed.8*
%{_mandir}/man8/innbind.8*
%{_mandir}/man8/inncheck.8*
%{_mandir}/man8/innd.8*
%{_mandir}/man8/inndf.8*
%{_mandir}/man8/innfeed.8*
%{_mandir}/man8/innreport.8*
%{_mandir}/man8/innstat.8*
%{_mandir}/man8/innupgrade.8*
%{_mandir}/man8/innwatch.8*
%{_mandir}/man8/innxbatch.8*
%{_mandir}/man8/innxmit.8*
%{_mandir}/man8/inpaths.8*
%{_mandir}/man8/mailpost.8*
%{_mandir}/man8/makedbz.8*
%{_mandir}/man8/makehistory.8*
%{_mandir}/man8/mod-active.8*
%{_mandir}/man8/news.daily.8*
%{_mandir}/man8/news2mail.8*
%{_mandir}/man8/ninpaths.8*
%{_mandir}/man8/nnrpd.8*
%{_mandir}/man8/nntpsend.8*
%{_mandir}/man8/ovdb_*.8*
%{_mandir}/man8/overchan.8*
%{_mandir}/man8/perl-nocem.8*
%{_mandir}/man8/procbatch.8*
%{_mandir}/man8/prunehistory.8*
%{_mandir}/man8/radius.8*
%{_mandir}/man8/rc.news.8*
%{_mandir}/man8/scanlogs.8*
%{_mandir}/man8/scanspool.8*
%{_mandir}/man8/send-nntp.8*
%{_mandir}/man8/send-uucp.8*
%{_mandir}/man8/sendinpaths.8*
%{_mandir}/man8/tally.control.8*
%{_mandir}/man8/tdx-util.8*
%{_mandir}/man8/tinyleaf.8*
%{_mandir}/man8/writelog.8*
%lang(pl) %{_mandir}/pl/man1/getlist.1*
%lang(pl) %{_mandir}/pl/man8/innd.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinn.so.2
%attr(755,root,root) %{_libdir}/libinnhist.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libinnhist.so.2
%attr(755,root,root) %{_libdir}/libstorage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstorage.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libinn.so
%attr(755,root,root) %{_libdir}/libinnhist.so
%attr(755,root,root) %{_libdir}/libstorage.so
%{_libdir}/libinn.la
%{_libdir}/libinnhist.la
%{_libdir}/libstorage.la
%{_includedir}
%{_mandir}/man3/clientlib.3*
%{_mandir}/man3/dbz.3*
%{_mandir}/man3/inndcomm.3*
%{_mandir}/man3/libauth.3*
%{_mandir}/man3/libinn.3*
%{_mandir}/man3/libinnhist.3*
%{_mandir}/man3/libstorage.3*
# XXX: too generic name?
%{_mandir}/man3/list.3*
%{_mandir}/man3/qio.3*
# XXX: too generic name?
%{_mandir}/man3/tst.3*
%{_mandir}/man3/uwildmat.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libinn.a
%{_libdir}/libinnhist.a
%{_libdir}/libstorage.a

%files -n inews
%defattr(644,root,root,755)
%attr(755,root,news) %{_bindir}/inews
%{_mandir}/man1/inews.1*
