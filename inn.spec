Summary:	INN, the InterNet News System (news server)
Summary(de):	das InterNet News System (News-Server)
Summary(fr):	INN, le système InterNet News (serveur de news)
Summary(pl):	INN, serwer nowinek 
Summary(tr):	INN, InterNet Haber Sistemi (haber sunucu)
Name: 		inn
Version:	2.2.2
Release: 	6
Copyright:	distributable
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://ftp.isc.org/isc/inn/%{name}-%{version}.tar.gz
Source1:	%{name}-default-active
Source2:	%{name}-default-distributions
Source3:	%{name}-default-newsgroups
Source4:	%{name}-etc-inn.conf
Source5:	%{name}-etc-newsfeeds
Source6:	%{name}-etc-nnrp.access
Source7:	%{name}.crontab
Source8:	%{name}.init
Source9:	%{name}-cnfsstat.cron
Source10:	%{name}.logrotate
Patch0:		ftp://ftp.nemoto.ecei.tohoku.ac.jp/pub/Net/IPv6/Patches/inn-2.2.1-v6-19991121.diff.gz
Patch1:		%{name}-PLD.patch
Patch2:		inn-install.patch
URL: 		http://www.isc.org/inn.html
Prereq: 	/sbin/chkconfig
Prereq:		/sbin/ldconfig
Prereq:		sed
Prereq:		fileutils
Requires: 	cleanfeed
Requires:	rc-scripts
Requires:	/etc/cron.d
Requires:	/etc/rc.d/init.d/functions
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/news

%description
INN is a news server, which can be set up to handle USENET news, as well
as private "newsfeeds".  There is a *LOT* of information about setting
up INN in /usr/share/doc -- read it.

%description -l pl
INN jest serwerem news, który mo¿na skonfigurowaæ do obs³ugi USENET-u,
jak równie¿ do obs³ugi ,,prywatnych'' grup w sieciach intranetowych.
Ca³e mnóstwo po¿ytecznych informacji o konfigurowaniu INN-a znajdziesz
w katalogu /usr/share/doc/inn-*.

%package devel
Summary:	INN header files and development documentations
Summary(de):	INN-Library
Summary(fr):	Bibliothèque INN
Summary(pl):	Pliki nag³ówkowe i dokumentacja programisty do inn-a
Summary(tr):	INN kitaplýðý
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This library is needed by several programs that interface to INN, such as
newsgate or tin.

%description -l de devel
Diese Library wird von mehreren Programmen benötigt, die mit INN
kommunizieren, etwa newsgate oder tin.

%description -l fr devel
Cette bibliothèque est nécessaire à plusieurs programmes qui s'interfacent
avec INN, comme newsgate ou tin.

%description -l pl devel
Biblioteka niezbêdna do dzia³ania kilku programów wspó³pracuj±cych z INN-em, takich jak newsgate czy tin. 

%description -l tr devel
INN ile arayüz gerektiren programlar için (newsgate, tin gibi) gereken bir
kitaplýktýr.

%package static
Summary:	Static INN libraries
Summary(pl):	Biblioteki statyczne do INN
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static INN libraries.

%description -l pl static
Biblioteki statyczne do INN.

%package -n inews
Summary:	Inews program (used for posting by inn and trn)
Summary(de):	Inews-Programm (für die Zustellung mit inn und trn) 
Summary(fr):	Programme inews (utilisé par inn et trn pour poster)
Summary(pl):	Inews - program do wysy³ania artyku³ów (u¿ywany przez inn i trn)
Summary(tr):	Haber biçimlendirme programý
Group:		Networking/News
Group(pl):	Sieciowe/News

%description -n inews
The inews program is used by some news readers to post news.
It does some consistency checking and header reformatting,
and forwards the article on to the news server specified in
inn.conf.

%description -l de -n inews
Das Programm 'inews' wird von manchen Newsreadern zum Senden
von Nachrichten verwendet. Es führt eine Konsistenzprüfung und Header-Neuf
ormatierung aus und leitet die Nachricht an den in 'inn.conf' 
angegebenen News-Server weiter. 

%description -l fr -n inews
Le programme inews est utilisé par certains lecteurs de news pour
poster les articles. Il effectue des vérifications et un reformatage
des en-têtes et fait suivre l'article au serveur de news spécifié dans inn.conf.

%description -l pl -n inews
Inews jest u¿ywany przez niektóre czytniki news do wysy³ania
artyku³ów. Sprawdza budowê artyku³u, przepisuje nag³ówek i wysy³a
do serwera news wyszczególnionego w inn.conf.

%description -l tr -n inews
inews programý bazý haber okuyucular tarafýndan haber yollamak amacýyla
kullanýlýr.  Program bazý güvenlik denetimleri ve baþlýk biçimlendirmesi
yaparak ve inn.conf dosyasýnda belirtilen haber sunucuya makaleyi yollar.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
touch innfeed/*.[ly]

rm -f config.cache
autoconf
libtoolize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
        --with-news-user=news \
        --with-news-group=news \
        --with-news-master=news \
        --with-db-dir=/var/state/news \
        --with-etc-dir=%{_sysconfdir} \
        --with-log-dir=/var/log/news \
        --with-run-dir=/var/run/news \
        --with-spool-dir=/var/spool/news \
        --with-lib-dir=%{_datadir}/news \
        --with-tmp-path=/var/spool/news/incoming/tmp \
        --with-perl \
        --with-sendmail=/usr/lib/sendmail \
        --enable-tagged-hash \
        --enable-merge-to-groups \
        --enable-pgp-verify \
	--enable-shared \
	--enable-static \
	--enable-libtool
#	--enable-ipv6 \
#	--enable-dual-socket

make all PATHFILTER=%{_datadir}/news/filter \
	PATHCONTROL=%{_datadir}/news/control \
	RNEWSPROGS=%{_bindir}

%install 
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{news,rc.d/init.d,cron.d,logrotate.d}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}/news
install -d $RPM_BUILD_ROOT%{_datadir}/news/{control,filter,auth}
install -d $RPM_BUILD_ROOT%{_includedir}/inn
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,5,8}
install -d $RPM_BUILD_ROOT/var/{run/news,state/news/backoff,log/{news,archiv/news}}
install -d $RPM_BUILD_ROOT/var/spool/news/{articles,overview,incoming/{tmp,bad},outgoing,archive,uniover,innfeed,cycbuffs}

make install \
	DESTDIR="$RPM_BUILD_ROOT" \
	PATHFILTER=%{_datadir}/news/filter \
	PATHCONTROL=%{_datadir}/news/control \
	RNEWSPROGS=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT/var/state/news/active
install %{SOURCE2} $RPM_BUILD_ROOT/var/state/news/distributions
install %{SOURCE3} $RPM_BUILD_ROOT/var/state/news/newsgroups
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/inn.conf
install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/newsfeeds
install %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/nnrp.access
install %{SOURCE7} $RPM_BUILD_ROOT/etc/cron.d/inn
install %{SOURCE8} $RPM_BUILD_ROOT/etc/rc.d/init.d/inn
install %{SOURCE9} $RPM_BUILD_ROOT%{_bindir}/cnfsstat.cron
install %{SOURCE10} $RPM_BUILD_ROOT/etc/logrotate.d/inn

mv $RPM_BUILD_ROOT%{_bindir}/c7unbatch.sh $RPM_BUILD_ROOT%{_bindir}/c7unbatch
mv $RPM_BUILD_ROOT%{_bindir}/gunbatch.sh $RPM_BUILD_ROOT%{_bindir}/gunbatch

rm -f $RPM_BUILD_ROOT/var/state/news/history

umask 002
touch $RPM_BUILD_ROOT/var/state/news/subscriptions
touch $RPM_BUILD_ROOT/var/state/news/history
touch $RPM_BUILD_ROOT/var/state/news/.news.daily
touch $RPM_BUILD_ROOT/var/state/news/active.times
touch $RPM_BUILD_ROOT/var/log/news/news.notice
touch $RPM_BUILD_ROOT/var/log/news/news.crit
touch $RPM_BUILD_ROOT/var/log/news/news.err

install include/clibrary.h	$RPM_BUILD_ROOT%{_includedir}/inn
install include/configdata.h	$RPM_BUILD_ROOT%{_includedir}/inn
install include/dbz.h		$RPM_BUILD_ROOT%{_includedir}/inn
install include/libinn.h	$RPM_BUILD_ROOT%{_includedir}/inn
install include/storage.h	$RPM_BUILD_ROOT%{_includedir}/inn

mv $RPM_BUILD_ROOT%{_datadir}/news/*.{a,la,so*} $RPM_BUILD_ROOT%{_libdir}

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_datadir} $RPM_BUILD_ROOT%{_bindir}/makehistory \
	-a $RPM_BUILD_ROOT/var/state/news/active \
	-i -r -f $RPM_BUILD_ROOT/var/state/news/history || :

#Fix perms in sample directory to avoid bogus dependencies
find samples -name "*.in" -exec chmod a-x {} \;

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[1358]/* \
	CONTRIBUTORS HISTORY README README.perl_hook README.tcl_hook \
	INSTALL ChangeLog COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig 

if [ -f /var/state/news/history ]; then
	cd /var/state/news
	%{_bindir}/makehistory -i -r
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news.news history.*
	chmod 644 history.*
else
	cd /var/state/news
	cp /dev/null history
	%{_bindir}/makehistory -i
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news.news history history.*
	chmod 644 history history.*
fi
[ -f /var/state/news/active.times ] || {
	touch /var/state/news/active.times
	chown news.news /var/state/news/active.times
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

[ -f /var/state/news/.news.daily ] || {
	touch /var/state/news/.news.daily
	chown news.news /var/state/.news.daily
	chmod 664 /var/state/news/.news.daily
}

if [ -f /etc/syslog.conf ]; then
  if ! grep -q INN /etc/syslog.conf; then
    sed 's/mail.none;/mail.none;news.none;/' < /etc/syslog.conf > /etc/syslog.conf.inn
    mv /etc/syslog.conf.inn /etc/syslog.conf
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

%postun
/sbin/ldconfig 

%files
%defattr(644,root,root,755)
%doc {CONTRIBUTORS,HISTORY,README,README.perl_hook,README.tcl_hook}.gz
%doc {INSTALL,ChangeLog,COPYRIGHT}.gz

# DB
%attr(750,news,news) %dir /var/state/news
%attr(750,news,news) %dir /var/state/news/backoff
%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/state/news/active
%attr(644,news,news) %config(noreplace) %verify(not size mtime md5) /var/state/news/distributions
%attr(644,news,news) %config(noreplace) %verify(not size mtime md5) /var/state/news/newsgroups
%attr(644,news,root) %config(noreplace) %verify(not size mtime md5) /var/state/news/subscriptions
%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/state/news/active.times
%attr(664,news,news) %ghost /var/state/news/.news.daily

# LOGS
%attr(640,root,root) /etc/logrotate.d/inn
%attr(750,news,news) %dir /var/log/news
%attr(750,news,news) %dir /var/log/archiv/news
%attr(770,news,news) %dir /var/run/news
%attr(664,news,news) %ghost /var/log/news/news.notice
%attr(660,news,news) %ghost /var/log/news/news.crit
%attr(660,news,news) %ghost /var/log/news/news.err

# SPOOL
%attr(750,news,news) %dir /var/spool/news
%attr(770,news,news) %dir /var/spool/news/cycbuffs
%attr(770,news,news) %dir /var/spool/news/innfeed
%attr(770,news,news) %dir /var/spool/news/incoming
%attr(770,news,news) %dir /var/spool/news/incoming/bad
%attr(770,news,news) %dir /var/spool/news/incoming/tmp
%attr(770,news,news) %dir /var/spool/news/outgoing
%attr(770,news,news) %dir /var/spool/news/archive
%attr(770,news,news) %dir /var/spool/news/overview
%attr(770,news,news) %dir /var/spool/news/uniover
%attr(770,news,news) %dir /var/spool/news/articles

# CRON PARTS
%attr(640,root,root) %config %verify(not size mtime md5) /etc/cron.d/inn

# RC-SCRIPT
%attr(754,root,root) /etc/rc.d/init.d/inn

# CONFIGS (INN is a one big config ;-)
%attr(755,root,root) %dir %{_sysconfdir}
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/actsync.cfg
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/actsync.ign
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/control.ctl
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/cycbuff.conf
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/expire.ctl
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/incoming.conf
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/inn.conf
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/innfeed.conf
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/innreport.conf
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/innwatch.ctl
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/motd.news
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/news2mail.cf
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nnrp.access
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nnrpd.track
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nntpsend.ctl
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/overview.ctl
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/passwd.nntp
%attr(640,news,news) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/storage.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/moderators
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/distrib.pats
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/newsfeeds
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/overview.fmt

%attr(755,root,news) %dir %{_datadir}/news
%attr(755,root,root) %dir %{_datadir}/news/control
%attr(755,root,root) %dir %{_datadir}/news/filter
%attr(755,root,root) %dir %{_datadir}/news/auth

%config %verify(not size mtime md5) %{_datadir}/news/innreport_inn.pm
%config %verify(not size mtime md5) %{_datadir}/news/innshellvars
%config %verify(not size mtime md5) %{_datadir}/news/innshellvars.pl
%config %verify(not size mtime md5) %{_datadir}/news/innshellvars.tcl

%config %verify(not size mtime md5) %{_datadir}/news/filter/filter_nnrpd.pl
%config %verify(not size mtime md5) %{_datadir}/news/filter/filter.tcl
%config %verify(not size mtime md5) %{_datadir}/news/filter/nnrpd_auth.pl
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

# SUID
%attr(4754,root,news) %{_bindir}/startinnfeed
%attr(4754,root,uucp) %{_bindir}/rnews

# LIBS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

# BINARIES
%attr(755,root,root) %{_bindir}/actived
%attr(755,root,root) %{_bindir}/actmerge
%attr(755,root,root) %{_bindir}/actsync
%attr(755,root,root) %{_bindir}/actsyncd
%attr(755,root,root) %{_bindir}/archive
%attr(755,root,root) %{_bindir}/batcher
%attr(755,root,root) %{_bindir}/buffchan
%attr(755,root,root) %{_bindir}/c7unbatch
%attr(755,root,root) %{_bindir}/cnfsstat
%attr(755,root,root) %{_bindir}/cnfsstat.cron
%attr(755,root,root) %{_bindir}/controlbatch
%attr(755,root,root) %{_bindir}/controlchan
%attr(755,root,root) %{_bindir}/convdate
%attr(755,root,root) %{_bindir}/crosspost
%attr(755,root,root) %{_bindir}/ctlinnd
%attr(755,root,root) %{_bindir}/cvtbatch
%attr(755,root,root) %{_bindir}/decode
%attr(755,root,root) %{_bindir}/encode
%attr(755,root,root) %{_bindir}/expire
%attr(755,root,root) %{_bindir}/expireindex
%attr(755,root,root) %{_bindir}/expireover
%attr(755,root,root) %{_bindir}/expirerm
%attr(755,root,root) %{_bindir}/fastrm
%attr(755,root,root) %{_bindir}/filechan
%attr(755,root,root) %{_bindir}/getlist
%attr(755,root,root) %{_bindir}/grephistory
%attr(755,root,root) %{_bindir}/gunbatch
%attr(755,root,root) %{_bindir}/inncheck
%attr(755,root,root) %{_bindir}/innconfval
%attr(755,root,root) %{_bindir}/innd
%attr(755,root,root) %{_bindir}/inndf
%attr(755,root,root) %{_bindir}/inndstart
%attr(755,root,root) %{_bindir}/innfeed
%attr(755,root,root) %{_bindir}/innfeed-convcfg
%attr(755,root,root) %{_bindir}/innmail
%attr(755,root,root) %{_bindir}/innreport
%attr(755,root,root) %{_bindir}/innstat
%attr(755,root,root) %{_bindir}/innwatch
%attr(755,root,root) %{_bindir}/innxbatch
%attr(755,root,root) %{_bindir}/innxmit
%attr(755,root,root) %{_bindir}/mailpost
%attr(755,root,root) %{_bindir}/makeactive
%attr(755,root,root) %{_bindir}/makehistory
%attr(755,root,root) %{_bindir}/mod-active
%attr(755,root,root) %{_bindir}/news2mail
%attr(755,root,root) %{_bindir}/news.daily
%attr(755,root,root) %{_bindir}/newsrequeue
%attr(755,root,root) %{_bindir}/nnrpd
%attr(755,root,root) %{_bindir}/nntpget
%attr(755,root,root) %{_bindir}/nntpsend
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
%attr(755,root,root) %{_bindir}/simpleftp
%attr(755,root,root) %{_bindir}/sm
%attr(755,root,root) %{_bindir}/tally.control
%attr(755,root,root) %{_bindir}/writelog

# MAN
%{_mandir}/man1/convdate.1*
%{_mandir}/man1/getlist.1*
%{_mandir}/man1/grephistory.1*
%{_mandir}/man1/innconfval.1*
%{_mandir}/man1/innfeed.1*
%{_mandir}/man1/installit.1*
%{_mandir}/man1/nntpget.1*
%{_mandir}/man1/rnews.1*
%{_mandir}/man1/shlock.1*
%{_mandir}/man1/shrinkfile.1*
%{_mandir}/man1/startinnfeed.1*
%{_mandir}/man1/subst.1*
%{_mandir}/man[58]/**

%files devel
%defattr(644,root,root,755)
%{_includedir}/inn/*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a

%files -n inews
%defattr(644,root,root,755)
%attr(2755,root,news) %{_bindir}/inews
%{_mandir}/man1/inews.1*
