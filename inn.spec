Summary:	INN, the InterNet News System (news server)
Summary(de):	das InterNet News System (News-Server)
Summary(fr):	INN, le système InterNet News (serveur de news)
Summary(pl):	INN, serwer nowinek 
Summary(tr):	INN, InterNet Haber Sistemi (haber sunucu)
Name: 		inn
Version:	2.2
Release: 	3
Copyright:	distributable
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://ftp.isc.org/isc/inn/%{name}-%{version}.tar.gz
Source1:	inn-default-active
Source2:	inn-default-distributions
Source3:	inn-default-newsgroups
Source4:	inn-cron-expire
Source5:	inn-cron-rnews
Source6:	inn-etc-nnrp.access
Source7:	inn-cron-nntpsend
Source8:	innd.init
Source9:	ftp://ftp.exit109.com/users/jeremy/cleanfeed-latest.tar.gz
Source10:	ftp://ftp.isc.org/pub/pgpcontrol/pgpverify-1.10
Patch0:		inn-rh.patch
URL: 		http://www.isc.org/inn.html
Requires: 	cleanfeed
Requires:	perl
Buildroot: 	/tmp/%{name}-%{version}-root
Prereq: 	/sbin/chkconfig

%description
INN is a news server, which can be set up to handle USENET news, as well
as private "newsfeeds".  There is a *LOT* of information about setting
up INN in /usr/doc -- read it.

%description -l pl
INN jest serwerem news, który mo¿na skonfigurowaæ do obs³ugi USENET-u,
jak równie¿ do obs³ugi ,,prywatnych'' grup w sieciach intranetowych.
Ca³e mnóstwo po¿ytecznych informacji o konfigurowaniu INN-a znajdziesz
w katalogu /usr/doc/inn-*.

%package devel
Summary:	INN-Library
Summary(de):	INN-Library
Summary(fr):	Bibliothèque INN
Summary(pl):	INN-biblioteka i pliki nag³ówkowe dla inn-a
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
%setup  -q 
%patch0 -p1

%build
touch innfeed/*.[ly]

rm -f config.cache
autoconf
libtoolize --copy --force
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
        --prefix=/usr \
	--sysconfdir=/etc/news \
        --with-news-user=news \
        --with-news-group=news \
        --with-news-master=news \
        --with-db-dir=/var/lib/news \
        --with-etc-dir=/etc/news \
        --with-log-dir=/var/log/news \
        --with-run-dir=/var/run/news \
        --with-spool-dir=/var/spool/news \
        --with-lib-dir=%{_libdir}/news/lib \
        --with-tmp-path=/var/spool/news/in.coming/tmp \
        --with-perl \
        --with-sendmail=%{_libdir}/sendmail \
        --enable-tagged-hash \
        --enable-merge-to-groups \
        --enable-pgp-verify \
	--enable-shared

make all

%install 
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,cron.{daily,hourly}}

make DESTDIR="$RPM_BUILD_ROOT" install

mv $RPM_BUILD_ROOT/usr/bin/rc.news $RPM_BUILD_ROOT/etc/rc.d

install $RPM_SOURCE_DIR/inn-default-active $RPM_BUILD_ROOT/var/lib/news/active
install $RPM_SOURCE_DIR/inn-default-distributions $RPM_BUILD_ROOT/var/lib/news/distributions
install $RPM_SOURCE_DIR/inn-default-newsgroups $RPM_BUILD_ROOT/var/lib/news/newsgroups

install $RPM_SOURCE_DIR/inn-cron-expire $RPM_BUILD_ROOT/etc/cron.daily/inn-cron-expire
install $RPM_SOURCE_DIR/inn-cron-rnews $RPM_BUILD_ROOT/etc/cron.daily/inn-cron-rnews
install $RPM_SOURCE_DIR/inn-cron-nntpsend $RPM_BUILD_ROOT/etc/cron.hourly/inn-cron-nntpsend

install $RPM_SOURCE_DIR/inn-etc-nnrp.access $RPM_BUILD_ROOT/etc/news/nnrp.access

install $RPM_SOURCE_DIR/innd.init $RPM_BUILD_ROOT/etc/rc.d/init.d/innd

rm -f $RPM_BUILD_ROOT/var/lib/news/history

umask 002
touch $RPM_BUILD_ROOT/var/lib/news/subscriptions
touch $RPM_BUILD_ROOT/var/lib/news/history
touch $RPM_BUILD_ROOT/var/lib/news/.news.daily
touch $RPM_BUILD_ROOT/var/log/news/news.notice
touch $RPM_BUILD_ROOT/var/log/news/news.crit
touch $RPM_BUILD_ROOT/var/log/news/news.err
touch $RPM_BUILD_ROOT/var/lib/news/active.times

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT/usr/bin/makehistory\
	-a $RPM_BUILD_ROOT/var/lib/news/active \
	-i -r -f $RPM_BUILD_ROOT/var/lib/news/history || :

#Fix perms in sample directory to avoid bogus dependencies
find samples -name "*.in" -exec chmod a-x {} \;

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/* \
	CONTRIBUTORS HISTORY README README.perl_hook README.tcl_hook \
	INSTALL ChangeLog COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lib/news/history ]; then
	cd /var/lib/news
	%{_libdir}/news/bin/makehistory -i -r
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news.news history.*
	chmod 644 history.*
else
	cd /var/lib/news
	cp /dev/null history
	%{_libdir}/news/bin/makehistory -i
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
chown -R news.news /var/log/news*
if [ -f /etc/syslog.conf ]; then
  if ! grep -q INN /etc/syslog.conf; then
    sed 's/mail.none;/mail.none;news.none;/' < /etc/syslog.conf > /etc/syslog.conf.inn
    mv /etc/syslog.conf.inn /etc/syslog.conf

    echo '' \
       >> /etc/syslog.conf
    echo '#' \
       >> /etc/syslog.conf
    echo '# INN' \
       >> /etc/syslog.conf
    echo '#' \
       >> /etc/syslog.conf
    echo 'news.=crit                                        /var/log/news/news.crit'   >> /etc/syslog.conf
    echo 'news.=err                                         /var/log/news/news.err'    >> /etc/syslog.conf
    echo 'news.notice                                       /var/log/news/news.notice' >> /etc/syslog.conf
    fi
  if [ -f /var/run/syslog.pid ]; then
    kill -HUP `cat /var/run/syslog.pid` 2> /dev/null ||:
  fi
else
  # syslog.conf does not exist

  echo "mail.none /var/log/messages" \
     >  /etc/syslog.conf.inn
  echo "" \
     >> /etc/syslog.conf.inn
  echo "# INN" \
     >> /etc/syslog.conf.inn
  echo "news.=crit                                      /var/log/news/news.crit"     >> /etc/syslog.conf.inn
  echo "news.=err                                       /var/log/news/news.err"      >> /etc/syslog.conf.inn
  echo "news.notice                                     /var/log/news/news.notice"   >> /etc/syslog.conf.inn
fi
if [ `cat /etc/news/inn.conf | grep '^server:' | wc -l` -lt 1 ]; then
  echo "server: `hostname -f`" >> /etc/news/inn.conf
fi

if [ `cat /etc/ld.so.conf | grep '^%{_libdir}/news/lib' | wc -l` -lt 0 ]; then
  echo '%{_libdir}/news/lib' >> /etc/ld.so.conf
fi
/sbin/chkconfig --add news
/sbin/ldconfig 

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/news ]; then
		/etc/rc.d/init.d/news stop
		/etc/rc.d/init.d/inn stop
	fi
	/sbin/chkconfig --del news
fi

%files
%defattr(644,root,root,755)
%doc {CONTRIBUTORS,HISTORY,README,README.perl_hook,README.tcl_hook}.gz
%doc {INSTALL,ChangeLog,COPYRIGHT}.gz

%attr(775,news,news) %dir /etc/news
%dir %{_libdir}/news
%dir /usr/bin
%dir /usr/bin/auth
%dir /usr/bin/control
%dir /usr/bin/filter
%dir /usr/bin/rnews.libexec
%dir %{_libdir}/news/lib
%dir /var/lib/news
%dir /var/lib/news/backoff
%attr(750,news,news) %dir /var/log/news
%attr(775,news,news) %dir /var/log/news/OLD
%attr(775,news,news) %dir /var/run/news
%attr(750,news,news) %dir /var/spool/news
%attr(775,news,news) %dir /var/spool/news/cycbuffs
%attr(775,news,news) %dir /var/spool/news/innfeed
%attr(775,news,news) %dir /var/spool/news/in.coming
%attr(775,news,news) %dir /var/spool/news/in.coming/bad
%attr(775,news,news) %dir /var/spool/news/in.coming/tmp
%attr(775,news,news) %dir /var/spool/news/out.going
%attr(775,news,news) %dir /var/spool/news/archive
%attr(775,news,news) %dir /var/spool/news/over.view
%attr(775,news,news) %dir /var/spool/news/uni.over

%attr(750,root,root) %config %verify(not size mtime md5) /etc/cron.daily/*
%attr(750,root,root) %config %verify(not size mtime md5) /etc/cron.hourly/*

%attr(754,news,news) %config /etc/rc.d/rc.news
%attr(754,root,root) %config /etc/rc.d/init.d/news

%attr(644,news,news) %config %verify(not size mtime md5) /etc/news/.news.daily
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/actsync.cfg
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/actsync.ign
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/control.ctl
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/cycbuff.conf
%attr(550,news,news) %config %verify(not size mtime md5) /etc/news/default
%attr(644,news,news) %config %verify(not size mtime md5) /etc/news/distrib.pats
%attr(550,news,news) %config %verify(not size mtime md5) /etc/news/docheckgroups
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/expire.ctl
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/incoming.conf
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/inn.conf
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/innfeed.conf
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/innreport.conf
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/innreport_inn.pm
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/innshellvars
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/innshellvars.pl
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/innshellvars.tcl
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/innwatch.ctl
%attr(644,news,news) %config %verify(not size mtime md5) /etc/news/moderators
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/motd.news
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/news2mail.cf
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/newsfeeds
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/nnrp.access
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/nnrpd.track
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/nntpsend.ctl
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/overview.ctl
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/overview.fmt
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/passwd.nntp
%attr(550,news,news) %config %verify(not size mtime md5) /etc/news/send-ihave
%attr(550,news,news) %config %verify(not size mtime md5) /etc/news/send-nntp
%attr(550,news,news) %config %verify(not size mtime md5) /etc/news/send-uucp
%attr(640,news,news) %config %verify(not size mtime md5) /etc/news/storage.conf

%attr(755,root,root) /usr/bin/rnews
%attr(755,root,root) /usr/bin/inews
%attr(755,root,root) /usr/sbin/ctlinnd
%attr(755,root,root) /usr/bin/actived
%attr(755,root,root) /usr/bin/actmerge
%attr(755,root,root) /usr/bin/actsync
%attr(755,root,root) /usr/bin/actsyncd
%attr(755,root,root) /usr/bin/archive
%attr(755,root,root) /usr/bin/batcher
%attr(755,root,root) /usr/bin/buffchan
%attr(755,root,root) /usr/bin/cnfsstat
%attr(755,root,root) /usr/bin/control/*
%attr(755,root,root) /usr/bin/controlbatch
%attr(755,root,root) /usr/bin/controlchan
%attr(755,root,root) /usr/bin/convdate
%attr(755,root,root) /usr/bin/crosspost
%attr(755,root,root) /usr/bin/ctlinnd
%attr(755,root,root) /usr/bin/cvtbatch
%attr(755,root,root) /usr/bin/expire
%attr(755,root,root) /usr/bin/expireindex
%attr(755,root,root) /usr/bin/expireover
%attr(755,root,root) /usr/bin/expirerm
%attr(755,root,root) /usr/bin/fastrm
%attr(755,root,root) /usr/bin/filechan
%attr(640,news,news) /usr/bin/filter/*
%attr(755,root,root) /usr/bin/getlist
%attr(755,root,root) /usr/bin/grephistory
%attr(2555,root,news) /usr/bin/inews
%attr(755,root,root) /usr/bin/inncheck
%attr(755,root,root) /usr/bin/innconfval
%attr(755,root,root) /usr/bin/innd
%attr(755,root,root) /usr/bin/inndf
%attr(4550,root,news) /usr/bin/inndstart
%attr(755,root,root) /usr/bin/innfeed-convcfg
%attr(755,root,root) /usr/bin/innmail
%attr(755,root,root) /usr/bin/innstat
%attr(755,root,root) /usr/bin/innwatch
%attr(755,root,root) /usr/bin/innxbatch
%attr(755,root,root) /usr/bin/innxmit
%attr(755,root,root) /usr/bin/mailpost
%attr(755,root,root) /usr/bin/makeactive
%attr(755,root,root) /usr/bin/makehistory
%attr(755,root,root) /usr/bin/mod-active
%attr(755,root,root) /usr/bin/news2mail
%attr(755,root,root) /usr/bin/newsrequeue
%attr(755,root,root) /usr/bin/nntpget
%attr(755,root,root) /usr/bin/nntpsend
%attr(755,root,root) /usr/bin/overchan
%attr(755,root,root) /usr/bin/procbatch
%attr(755,root,root) /usr/bin/prunehistory
%attr(755,root,root) /usr/bin/pullnews
%attr(755,root,root) /usr/bin/rnews.libexec/*
%attr(755,root,root) /usr/bin/scanlogs
%attr(755,root,root) /usr/bin/scanspool
%attr(755,root,root) /usr/bin/send-*
%attr(755,root,root) /usr/bin/sendxbatches
%attr(755,root,root) /usr/bin/shlock
%attr(755,root,root) /usr/bin/shrinkfile
%attr(755,root,root) /usr/bin/simpleftp
%attr(755,root,root) /usr/bin/sm
%attr(755,root,root) %config /usr/bin/innfeed
%attr(755,root,root) %config /usr/bin/innreport
%attr(755,root,root) %config /usr/bin/news.daily
%attr(755,root,root) %config /usr/bin/nnrpd
%attr(755,root,root) %config /usr/bin/parsecontrol
%attr(755,root,root) %config /usr/bin/pgpverify
%attr(755,root,root) %config /usr/bin/rc.news
%attr(4550,root,uucp) %config /usr/bin/rnews
%attr(4550,root,news) %config /usr/bin/startinnfeed
%attr(755,root,root) /usr/bin/tally.control
%attr(755,root,root) /usr/bin/writelog

%config(missingok) %{_libdir}/news/lib/innreport_inn.pm
%config(missingok) %{_libdir}/news/lib/innshellvars
%config(missingok) %{_libdir}/news/lib/innshellvars.pl
%config(missingok) %{_libdir}/news/lib/innshellvars.tcl

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
%{_mandir}/man[58]/*

%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/active
%attr(644,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/distributions
%attr(644,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/newsgroups
%attr(644,news,root) %config(noreplace) %verify(not size mtime md5) /var/lib/news/subscriptions
%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/active.times
%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/log/news/news.notice
%attr(660,news,news) %config(noreplace) %verify(not size mtime md5) /var/log/news/news.crit
%attr(660,news,news) %config(noreplace) %verify(not size mtime md5) /var/log/news/news.err

%files devel
%defattr(644,root,root,755)
/usr/include/*
%{_libdir}/*.a
%{_mandir}/man3/*

%files -n inews
%defattr(644,root,root,755)

%attr(755,root,root) /usr/bin/inews
%attr(4555,news,news) %config /usr/bin/inews
%{_mandir}/man1/inews.1*

%changelog
* Fri May 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- man pages moved to /usr/share/ma (FHS 2.0 compiliat),
- removed not neccessary uid/gid=(news),
- changed install prefix to /usr.

* Mon Apr 19 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.2-3]
- recompiled on new rpm.

* Fri Apr 16 1999 Piotr Czerwiñski <pius@pld.org.pl>
- changed install procedure to allow building package from non-root 
  account (inn-install.patch),
- minor fixes.

* Thu Apr 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
- fixed Group(pl),
- changed Buildroot to /tmp/%{name}-%{version}-root,
- removed man group from man pages,
- added full %defattr description in %files,
- added Requires: %%{name} = %%{version} to devel subpackage,
- added some %requires_pkg macros,
- cosmetic changes for common l&f.

* Fri Jan 29 1999 Maciej Paliwoda <maciejp@uci.agh.edu.p>
  [2.2-1d]
- special thanks for Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
	& Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- new version 2.2 (stable)
- build for Linux PLD
- default storage CNFS
