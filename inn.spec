%include	/usr/lib/rpm/macros.perl
Summary:	INN, the InterNet News System (news server)
Summary(de):	das InterNet News System (News-Server)
Summary(es):	INN, InterNet News System (servidor news)
Summary(fr):	INN, le syst�me InterNet News (serveur de news)
Summary(pl):	INN, serwer nowinek 
Summary(pt_BR):	INN, InterNet News System (servidor news)
Summary(tr):	INN, InterNet Haber Sistemi (haber sunucu)
Name:		inn
Version:	2.3.2
Release:	6
License:	Distributable
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	ftp://ftp.isc.org/isc/inn/%{name}-%{version}.tar.gz
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
#Patch0:	ftp://ftp.north.ad.jp/pub/IPv6/INN/tmp/%{name}-2.3.0-v6-20001011.diff.gz
Patch0:		%{name}-ipv6.patch
Patch1:		%{name}-PLD.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-db3.patch
Patch4:		%{name}-setreuid.patch
Patch5:		%{name}-sec.patch
Patch6:		%{name}-frsize.patch
Patch7:		%{name}-ac25x.patch
URL:		http://www.isc.org/inn.html
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	db3-devel
BuildRequires:	openssl-devel >= 0.9.6a
BuildRequires:	perl-devel >= 5.6.1
Requires:	cleanfeed >= 0.95.7b-4
Requires:	rc-scripts >= 0.2.0
Requires:	/etc/cron.d
Requires:	psmisc >= 20.1
Requires:	util-linux
Prereq:		/sbin/chkconfig
Prereq:		/sbin/ldconfig
Prereq:		rc-scripts
Prereq:		sed
Prereq:		fileutils
Prereq:		%{name}-libs = %{version}
Provides:	nntpserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/news

# /usr/bin/pullnews doesn't provide perl(Net::NNTP) - perl-libnet does.
%define		_noautoprov	"perl(Net::NNTP)"
# it's necessary only for sample nnrpd_auth.pl hook
%define		_noautoreq	"perl(CDB_File)"

%description
INN is a news server, which can be set up to handle USENET news, as
well as private "newsfeeds". There is a *LOT* of information about
setting up INN in /usr/share/doc -- read it.

If you want innreport to generate graphs you need perl-GD package.

%description -l es
INN es un servidor de news, que puede ser configurado para manipular
USENET news bien como newsfeeds privadas. Existe un *Mont�n* de
informaci�n sobre la configuraci�n del INN en /usr/doc -- l�ela.

%description -l pl
INN jest serwerem news, kt�ry mo�na skonfigurowa� do obs�ugi USENET-u,
jak r�wnie� do obs�ugi ,,prywatnych'' grup w sieciach intranetowych.
Ca�e mn�stwo po�ytecznych informacji o konfigurowaniu INN-a znajdziesz
w katalogu /usr/share/doc/inn-*.

Je�li chcesz �eby innreport generowa� wykresy musisz zainstalowa�
pakiet perl-GD.

%description -l pt_BR
INN � um servidor de news, que pode ser configurado para manipular
USENET news bem como newsfeeds privadas. Existe um *MONTE* de
informa��es sobre a configura��o do INN em /usr/doc -- leia.

%package libs
Summary:	INN libraries
Summary(de):	INN-Library
Summary(fr):	Biblioth�que INN
Summary(pl):	Biblioteki do INN-a
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����

%description libs
This library is needed by several programs that interface to INN, such
as newsgate or tin.

%description -l de libs
Diese Library wird von mehreren Programmen ben�tigt, die mit INN
kommunizieren, etwa newsgate oder tin.

%description -l fr libs
Cette biblioth�que est n�cessaire � plusieurs programmes qui
s'interfacent avec INN, comme newsgate ou tin.

%description -l pl libs
Biblioteka niezb�dna do dzia�ania kilku program�w wsp�pracuj�cych z
INN-em, takich jak newsgate czy tin.

%description -l tr libs
INN ile aray�z gerektiren programlar i�in (newsgate, tin gibi) gereken
bir kitapl�kt�r.

%package devel
Summary:	INN header files and development documentations
Summary(de):	INN-Library
Summary(es):	Biblioteca INN
Summary(fr):	Biblioth�que INN
Summary(pl):	Pliki nag��wkowe i dokumentacja programisty do inn-a
Summary(pt_BR):	Biblioteca INN
Summary(tr):	INN kitapl���
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-libs = %{version}
Requires:	db3-devel

%description devel
Header files and developer documentations for INN libraries.

%description -l de devel
Diese Library wird von mehreren Programmen ben�tigt, die mit INN
kommunizieren, etwa newsgate oder tin.

%description -l es devel
Esta biblioteca es requerida por varios programas que tienen interface
con INN, como el newsgate o tin.

%description -l fr devel
Cette biblioth�que est n�cessaire � plusieurs programmes qui
s'interfacent avec INN, comme newsgate ou tin.

%description -l pl devel
Pliki nag��wkowe i dokumentacja programisty do bibliotek INN-a.

%description -l pt_BR devel
Esta biblioteca � requerida por v�rios programas que tem interface com
o INN, como o newsgate ou tin.

%description -l tr devel
INN ile aray�z gerektiren programlar i�in (newsgate, tin gibi) gereken
bir kitapl�kt�r.

%package static
Summary:	Static INN libraries
Summary(es):	Static libraries for inn development
Summary(pl):	Biblioteki statyczne do INN
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com inn
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static INN libraries.

%description -l es static
Static libraries for inn development

%description -l pl static
Biblioteki statyczne do INN.

%description -l pt_BR static
INN � um servidor de news, que pode ser configurado para manipular
USENET news bem como newsfeeds privadas. Existe um *MONTE* de
informa��es sobre a configura��o do INN em /usr/doc -- leia.

Bibliotecas est�ticas para desenvolvimento com inn

%package -n inews
Summary:	Inews program (used for posting by inn and trn)
Summary(de):	Inews-Programm (f�r die Zustellung mit inn und trn) 
Summary(es):	Programa Inews (usado para franqueo por inn y trn)
Summary(fr):	Programme inews (utilis� par inn et trn pour poster)
Summary(pl):	Inews - program do wysy�ania artyku��w (u�ywany przez inn i trn)
Summary(pt_BR):	Programa Inews (usado para postagem pelo inn e trn)
Summary(tr):	Haber bi�imlendirme program�
Group:		Networking/News
Group(de):	Netzwerkwesen/News
Group(pl):	Sieciowe/News

%description -n inews
The inews program is used by some news readers to post news. It does
some consistency checking and header reformatting, and forwards the
article on to the news server specified in inn.conf.

%description -l de -n inews
Das Programm 'inews' wird von manchen Newsreadern zum Senden von
Nachrichten verwendet. Es f�hrt eine Konsistenzpr�fung und Header-Neuf
ormatierung aus und leitet die Nachricht an den in 'inn.conf'
angegebenen News-Server weiter.

%description -l es -n inews
El programa inews se usa por algunos lectores de news para postar
mensajes. Hace alguna consistencia chequeando y reformateando headers,
y enviando el art�culo para el servidor de news especificado en el
inn.conf.

%description -l fr -n inews
Le programme inews est utilis� par certains lecteurs de news pour
poster les articles. Il effectue des v�rifications et un reformatage
des en-t�tes et fait suivre l'article au serveur de news sp�cifi� dans
inn.conf.

%description -l pl -n inews
Inews jest u�ywany przez niekt�re czytniki news do wysy�ania
artyku��w. Sprawdza budow� artyku�u, przepisuje nag��wek i wysy�a do
serwera news wyszczeg�lnionego w inn.conf.

%description -l pt_BR -n inews
O programa inews � usado por alguns leitores de news para postar
mensagens. Ele faz alguma consist�ncia checando e reformatando
headers, e enviando o artigo para o servidor de news especificado no
inn.conf.

%description -l tr -n inews
inews program� baz� haber okuyucular taraf�ndan haber yollamak
amac�yla kullan�l�r. Program baz� g�venlik denetimleri ve ba�l�k
bi�imlendirmesi yaparak ve inn.conf dosyas�nda belirtilen haber
sunucuya makaleyi yollar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
touch innfeed/*.[ly]

rm -f config.cache
autoconf
libtoolize --copy --force
%configure \
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
	%{?_with_largefiles:--with-largefiles} \
        %{!?_with_largefiles:--enable-tagged-hash} \
        --enable-merge-to-groups \
        --enable-pgp-verify \
	--enable-shared \
	--enable-static \
	--enable-libtool \
	--enable-ipv6 \
	--enable-dual-socket

%{__make} all PATHFILTER=%{_datadir}/news/filter \
	PATHCONTROL=%{_datadir}/news/control

%install 
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{news,rc.d/init.d,cron.d,logrotate.d} \
	$RPM_BUILD_ROOT{%{_libdir}/news/{rnews,auth/generic},%{_includedir}/inn} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/news/{control,filter,auth}} \
	$RPM_BUILD_ROOT%{_mandir}/man{1,3,5,8} \
	$RPM_BUILD_ROOT/var/{run/news,lib/news/backoff,log/{news,archiv/news}} \
	$RPM_BUILD_ROOT/var/spool/news/{articles,overview,incoming/{tmp,bad},outgoing,archive,uniover,innfeed,cycbuffs}

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
install %{SOURCE10} $RPM_BUILD_ROOT/%{_sysconfdir}/readers.conf

rm -f $RPM_BUILD_ROOT/var/lib/news/history

umask 002
touch $RPM_BUILD_ROOT/var/lib/news/subscriptions
touch $RPM_BUILD_ROOT/var/lib/news/history
touch $RPM_BUILD_ROOT/var/lib/news/.news.daily
touch $RPM_BUILD_ROOT/var/lib/news/active.times
touch $RPM_BUILD_ROOT/var/log/news/news.notice
touch $RPM_BUILD_ROOT/var/log/news/news.crit
touch $RPM_BUILD_ROOT/var/log/news/news.err

touch $RPM_BUILD_ROOT%{_includedir}/inn/configdata.h	
install include/{clibrary,dbz,libinn,nntp,ov,qio,ppport,rwlock,storage}.h \
	$RPM_BUILD_ROOT%{_includedir}/inn

mv -f $RPM_BUILD_ROOT%{_datadir}/news/*.{a,la,so*} $RPM_BUILD_ROOT%{_libdir}

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_datadir} $RPM_BUILD_ROOT%{_bindir}/makehistory \
	-a $RPM_BUILD_ROOT/var/lib/news/active \
	-i -r -f $RPM_BUILD_ROOT/var/lib/news/history || :

#Fix perms in sample directory to avoid bogus dependencies
find samples -name "*.in" -exec chmod a-x {} \;

gzip -9nf CONTRIBUTORS INSTALL HISTORY README* ChangeLog LICENSE NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lib/news/history ]; then
	cd /var/lib/news
	%{_bindir}/makedbz -s `wc -l <history` -f history
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news.news history.*
	chmod 644 history.*
else
	cd /var/lib/news
	cp /dev/null history
	%{_bindir}/makehistory
	%{_bindir}/makedbz -s `wc -l <history` -f history
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news.news history history.*
	chmod 644 history history.*
fi
[ -f /var/lib/news/active.times ] || {
	touch /var/lib/news/active.times
	chown news.news /var/lib/news/active.times
}

[ -f /var/log/news/news.notice ] || {
	touch /var/log/news/news.notice
	chown news.news /var/log/news/news.notice
	chmod 664 /var/log/news/news.notice
}

[ -f /var/log/news/news.crit ] || {
	touch /var/log/news/news.crit
	chown news.news /var/log/news/news.crit
	chmod 660 /var/log/news/news.crit
}

[ -f /var/log/news/news.err ] || {
	touch /var/log/news/news.err
	chown news.news /var/log/news/news.err
	chmod 660 /var/log/news/news.err
}

[ -f /var/lib/news/.news.daily ] || {
	touch /var/lib/news/.news.daily
	chown news.news /var/lib/news/.news.daily
	chmod 664 /var/lib/news/.news.daily
}

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

%post libs -p /sbin/ldconfig 
%postun libs -p /sbin/ldconfig 

%files
%defattr(644,root,root,755)
%doc {CONTRIBUTORS,INSTALL,HISTORY,README*,ChangeLog,LICENSE,NEWS}.gz

# DB
%attr(770,root,news) %dir /var/lib/news
%attr(770,root,news) %dir /var/lib/news/backoff
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/active
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/distributions
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/newsgroups
%attr(664,root,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/subscriptions
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
%attr(640,root,root) %config %verify(not size mtime md5) /etc/cron.d/inn

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

%attr(755,root,news) %dir %{_datadir}/news
%attr(755,root,root) %dir %{_datadir}/news/control
%attr(755,root,root) %dir %{_datadir}/news/filter

%attr(755,root,root) %{_datadir}/news/docheckgroups
%config %verify(not size mtime md5) %{_datadir}/news/innreport_inn.pm
%config %verify(not size mtime md5) %{_datadir}/news/innshellvars
%config %verify(not size mtime md5) %{_datadir}/news/innshellvars.pl
%config %verify(not size mtime md5) %{_datadir}/news/innshellvars.tcl

%config %verify(not size mtime md5) %{_datadir}/news/filter/INN.py
%config %verify(not size mtime md5) %{_datadir}/news/filter/filter_nnrpd.pl
%config %verify(not size mtime md5) %{_datadir}/news/filter/filter.tcl
%config %verify(not size mtime md5) %{_datadir}/news/filter/nnrpd_auth.pl
%config %verify(not size mtime md5) %{_datadir}/news/filter/nnrpd_auth.py
%config %verify(not size mtime md5) %{_datadir}/news/filter/startup_innd.pl
%config %verify(not size mtime md5) %{_datadir}/news/filter/startup.tcl

%attr(755,root,root) %{_datadir}/news/control/checkgroups
%attr(755,root,root) %{_datadir}/news/control/checkgroups.pl
%attr(755,root,root) %{_datadir}/news/control/default
%attr(755,root,root) %{_datadir}/news/control/ihave
%attr(755,root,root) %{_datadir}/news/control/ihave.pl
%attr(755,root,root) %{_datadir}/news/control/newgroup
%attr(755,root,root) %{_datadir}/news/control/newgroup.pl
%attr(755,root,root) %{_datadir}/news/control/rmgroup
%attr(755,root,root) %{_datadir}/news/control/rmgroup.pl
%attr(755,root,root) %{_datadir}/news/control/sendme
%attr(755,root,root) %{_datadir}/news/control/sendme.pl
%attr(755,root,root) %{_datadir}/news/control/sendsys
%attr(755,root,root) %{_datadir}/news/control/sendsys.pl
%attr(755,root,root) %{_datadir}/news/control/senduuname
%attr(755,root,root) %{_datadir}/news/control/senduuname.pl
%attr(755,root,root) %{_datadir}/news/control/version
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
%attr(4754,root,uucp) %{_bindir}/rnews

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
%attr(755,root,root) %{_bindir}/dbprocs
%attr(755,root,root) %{_bindir}/expire
%attr(755,root,root) %{_bindir}/expireover
%attr(755,root,root) %{_bindir}/expirerm
%attr(755,root,root) %{_bindir}/fastrm
%attr(755,root,root) %{_bindir}/filechan
%attr(755,root,root) %{_bindir}/getlist
%attr(755,root,root) %{_bindir}/grephistory
%attr(755,root,root) %{_bindir}/inncheck
%attr(755,root,root) %{_bindir}/innconfval
%attr(755,root,root) %{_bindir}/innd
%attr(755,root,root) %{_bindir}/inndf
%attr(755,root,root) %{_bindir}/innfeed
%attr(755,root,root) %{_bindir}/innmail
%attr(755,root,root) %{_bindir}/innreport
%attr(755,root,root) %{_bindir}/innstat
%attr(755,root,root) %{_bindir}/innwatch
%attr(755,root,root) %{_bindir}/innxbatch
%attr(755,root,root) %{_bindir}/innxmit
%attr(755,root,root) %{_bindir}/mailpost
%attr(755,root,root) %{_bindir}/makedbz
%attr(755,root,root) %{_bindir}/makehistory
%attr(755,root,root) %{_bindir}/mod-active
%attr(755,root,root) %{_bindir}/news.daily
%attr(755,root,root) %{_bindir}/news2mail
%attr(755,root,root) %{_bindir}/newsrequeue
%attr(755,root,root) %{_bindir}/nnrpd
%attr(755,root,root) %{_bindir}/nntpget
%attr(755,root,root) %{_bindir}/nntpsend
%attr(755,root,root) %{_bindir}/ovdb_*
%attr(755,root,root) %{_bindir}/overchan
%attr(755,root,root) %{_bindir}/parsecontrol
%attr(755,root,root) %{_bindir}/pgpverify
%attr(755,root,root) %{_bindir}/procbatch
%attr(755,root,root) %{_bindir}/prunehistory
%attr(755,root,root) %{_bindir}/pullnews
%attr(755,root,root) %{_bindir}/scanlogs
%attr(755,root,root) %{_bindir}/scanspool
%attr(755,root,root) %{_bindir}/sendbatch
%attr(755,root,root) %{_bindir}/send-ihave
%attr(755,root,root) %{_bindir}/send-nntp
%attr(755,root,root) %{_bindir}/send-uucp
%attr(755,root,root) %{_bindir}/sendxbatches
%attr(755,root,root) %{_bindir}/shlock
%attr(755,root,root) %{_bindir}/shrinkfile
%attr(755,root,root) %{_bindir}/signcontrol
%attr(755,root,root) %{_bindir}/simpleftp
%attr(755,root,root) %{_bindir}/sm
%attr(755,root,root) %{_bindir}/tally.control
%attr(755,root,root) %{_bindir}/writelog

# MAN
%{_mandir}/man1/ckpasswd.1*
%{_mandir}/man1/convdate.1*
%{_mandir}/man1/getlist.1*
%{_mandir}/man1/grephistory.1*
%{_mandir}/man1/innconfval.1*
%{_mandir}/man1/innfeed.1*
%{_mandir}/man1/nntpget.1*
%{_mandir}/man1/rnews.1*
%{_mandir}/man1/shlock.1*
%{_mandir}/man1/shrinkfile.1*
%{_mandir}/man1/simpleftp.1*
%{_mandir}/man1/startinnfeed.1*
%{_mandir}/man[58]/**

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/inn
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
