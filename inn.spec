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
Source6:	news.init
Patch0: 	inn-all.patch
Url: 		http://www.isc.org/inn.html
Requires: 	cleanfeed
%requires_pkg	perl
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
%setup -q 
%patch0 -p1

%build
touch innfeed/*.[ly]

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
        --prefix=/usr/lib/news \
        --mandir=/usr/man \
        --with-news-user=news \
        --with-news-group=news \
        --with-news-master=news \
        --with-db-dir=/var/lib/news \
        --with-etc-dir=/etc/news \
        --with-log-dir=/var/log/news \
        --with-run-dir=/var/run/news \
        --with-spool-dir=/var/spool/news \
        --with-lib-dir=/usr/lib/news/lib \
        --with-tmp-path=/var/spool/news/in.coming/tmp \
        --with-perl \
        --with-sendmail=/usr/lib/sendmail \
        --enable-tagged-hash \
        --enable-merge-to-groups \
        --enable-pgp-verify \
	--enable-shared
make all

%install 
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/{news,rc.d/init.d,news},etc/cron.{daily,hourly}}
install -d $RPM_BUILD_ROOT/{usr/{lib/{news/{bin,lib}},bin,sbin,include,man/{man{1,3,5,8}}}}
install -d $RPM_BUILD_ROOT/{var/{lib/news/backoff,spool/news/{in.coming/{bad,tmp},cycbuffs,innfeed,archive,out.going,over.view,uni.over}}}
install -d $RPM_BUILD_ROOT/{var/{lock/news,log/news/OLD,run/news}}

make DESTDIR="$RPM_BUILD_ROOT" install
install %{SOURCE1} $RPM_BUILD_ROOT/var/lib/news/active
install %{SOURCE2} $RPM_BUILD_ROOT/var/lib/news/distributions
install %{SOURCE3} $RPM_BUILD_ROOT/var/lib/news/newsgroups
install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/inn-cron-expire
install %{SOURCE5} $RPM_BUILD_ROOT/etc/cron.daily/inn-cron-rnews
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/news
install samples/nntpsend $RPM_BUILD_ROOT/etc/cron.hourly/inn-cron-nntpsend

install samples/default $RPM_BUILD_ROOT/etc/news
install samples/docheckgroups $RPM_BUILD_ROOT/etc/news
install samples/innreport_inn.pm $RPM_BUILD_ROOT/etc/news
install samples/innshellvars $RPM_BUILD_ROOT/etc/news
install samples/innshellvars.pl $RPM_BUILD_ROOT/etc/news
install samples/innshellvars.tcl $RPM_BUILD_ROOT/etc/news
install samples/send-ihave $RPM_BUILD_ROOT/etc/news
install samples/send-nntp $RPM_BUILD_ROOT/etc/news
install samples/send-uucp $RPM_BUILD_ROOT/etc/news
install /dev/null $RPM_BUILD_ROOT/etc/news/.news.daily
install $RPM_BUILD_ROOT/usr/lib/news/bin/rc.news $RPM_BUILD_ROOT/etc/rc.d/rc.news

ln -sf /usr/lib/news/bin/ctlinnd $RPM_BUILD_ROOT/usr/sbin/ctlinnd
ln -sf ../lib/news/bin/rnews $RPM_BUILD_ROOT/usr/bin/rnews
ln -sf ../lib/news/bin/inews $RPM_BUILD_ROOT/usr/bin/inews
ln -sf /etc/news/innshellvars $RPM_BUILD_ROOT/usr/lib/news/lib/innshellvars
ln -sf /etc/news/innshellvars.pl $RPM_BUILD_ROOT/usr/lib/news/lib/innshellvars.pl
ln -sf /etc/news/innshellvars.tcl $RPM_BUILD_ROOT/usr/lib/news/lib/innshellvars.tcl

install /dev/null $RPM_BUILD_ROOT/var/lib/news/subscriptions
install /dev/null $RPM_BUILD_ROOT/var/lib/news/active.times

install /dev/null $RPM_BUILD_ROOT/var/log/news/news.notice
install /dev/null $RPM_BUILD_ROOT/var/log/news/news.crit
install /dev/null $RPM_BUILD_ROOT/var/log/news/news.err

install lib/libinn.a $RPM_BUILD_ROOT/usr/lib
install storage/libstorage.a $RPM_BUILD_ROOT/usr/lib
install include/configdata.h $RPM_BUILD_ROOT/usr/include
install include/dbz.h $RPM_BUILD_ROOT/usr/include
install include/libinn.h $RPM_BUILD_ROOT/usr/include
install include/storage.h $RPM_BUILD_ROOT/usr/include
install include/clibrary.h $RPM_BUILD_ROOT/usr/include
install storage/interface.h $RPM_BUILD_ROOT/usr/include
install storage/methods.h $RPM_BUILD_ROOT/usr/include
install storage/overview.h $RPM_BUILD_ROOT/usr/include

gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,3,5,8}/* \
	CONTRIBUTORS HISTORY README README.perl_hook README.tcl_hook

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lib/news/history ]; then
	cd /var/lib/news
	/usr/lib/news/bin/makehistory -i -r
	for i in dir hash index pag; do
		[ -f history.n.$i ] && mv history.n.$i history.$i
	done
	chown news.news history.*
	chmod 644 history.*
else
	cd /var/lib/news
	cp /dev/null history
	/usr/lib/news/bin/makehistory -i
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

if [ `cat /etc/ld.so.conf | grep '^/usr/lib/news/lib' | wc -l` -lt 0 ]; then
  echo '/usr/lib/news/lib' >> /etc/ld.so.conf
fi
/sbin/chkconfig --add news
/sbin/ldconfig 

%preun
if [ $1 = 0 ]; then
   if [ -f /var/lock/subsys/news ]; then
       /etc/rc.d/init.d/news stop
       /etc/rc.d/init.d/inn stop
   fi
   /sbin/chkconfig --del news
fi

%files
%defattr(644,root,root,755)
%doc {CONTRIBUTORS,HISTORY,README,README.perl_hook,README.tcl_hook}.gz

%attr(775,news,news) %dir /etc/news
%attr(755,news,news) %dir /usr/lib/news
%attr(755,news,news) %dir /usr/lib/news/bin
%attr(755,news,news) %dir /usr/lib/news/bin/auth
%attr(750,news,news) %dir /usr/lib/news/bin/control
%attr(750,news,news) %dir /usr/lib/news/bin/filter
%attr(750,news,news) %dir /usr/lib/news/bin/rnews.libexec
%attr(755,news,news) %dir /usr/lib/news/lib
%attr(755,news,news) %dir /var/lib/news
%attr(775,news,news) %dir /var/lib/news/backoff
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

%attr(711,root,root) /usr/bin/rnews
%attr(755,root,root) /usr/bin/inews
%attr(711,root,root) /usr/sbin/ctlinnd
%attr(555,news,news) /usr/lib/news/bin/actived
%attr(555,news,news) /usr/lib/news/bin/actmerge
%attr(555,news,news) /usr/lib/news/bin/actsync
%attr(555,news,news) /usr/lib/news/bin/actsyncd
%attr(555,news,news) /usr/lib/news/bin/archive
%attr(555,news,news) /usr/lib/news/bin/batcher
%attr(550,news,news) /usr/lib/news/bin/buffchan
%attr(550,news,news) /usr/lib/news/bin/cnfsstat
%attr(550,news,news) /usr/lib/news/bin/control/*
%attr(550,news,news) /usr/lib/news/bin/controlbatch
%attr(550,news,news) /usr/lib/news/bin/controlchan
%attr(555,news,news) /usr/lib/news/bin/convdate
%attr(550,news,news) /usr/lib/news/bin/crosspost
%attr(550,news,news) /usr/lib/news/bin/ctlinnd
%attr(555,news,news) /usr/lib/news/bin/cvtbatch
%attr(550,news,news) /usr/lib/news/bin/expire
%attr(550,news,news) /usr/lib/news/bin/expireindex
%attr(550,news,news) /usr/lib/news/bin/expireover
%attr(555,news,news) /usr/lib/news/bin/expirerm
%attr(550,news,news) /usr/lib/news/bin/fastrm
%attr(555,news,news) /usr/lib/news/bin/filechan
%attr(640,news,news) /usr/lib/news/bin/filter/*
%attr(550,news,news) /usr/lib/news/bin/getlist
%attr(555,news,news) /usr/lib/news/bin/grephistory
%attr(2511,news,news) /usr/lib/news/bin/inews
%attr(550,news,news) /usr/lib/news/bin/inncheck
%attr(550,news,news) /usr/lib/news/bin/innconfval
%attr(550,news,news) /usr/lib/news/bin/innd
%attr(550,news,news) /usr/lib/news/bin/inndf
%attr(4510,root,news) /usr/lib/news/bin/inndstart
%attr(550,news,news) %config /usr/lib/news/bin/innfeed
%attr(550,news,news) /usr/lib/news/bin/innfeed-convcfg
%attr(550,news,news) /usr/lib/news/bin/innmail
%attr(550,news,news) %config /usr/lib/news/bin/innreport
%attr(550,news,news) /usr/lib/news/bin/innstat
%attr(550,news,news) /usr/lib/news/bin/innwatch
%attr(550,news,news) /usr/lib/news/bin/innxbatch
%attr(550,news,news) /usr/lib/news/bin/innxmit
%attr(550,news,news) /usr/lib/news/bin/mailpost
%attr(550,news,news) /usr/lib/news/bin/makeactive
%attr(550,news,news) /usr/lib/news/bin/makehistory
%attr(550,news,news) /usr/lib/news/bin/mod-active
%attr(550,news,news) %config /usr/lib/news/bin/news.daily
%attr(550,news,news) /usr/lib/news/bin/news2mail
%attr(550,news,news) /usr/lib/news/bin/newsrequeue
%attr(550,news,news) %config /usr/lib/news/bin/nnrpd
%attr(550,news,news) /usr/lib/news/bin/nntpget
%attr(550,news,news) /usr/lib/news/bin/nntpsend
%attr(550,news,news) /usr/lib/news/bin/overchan
%attr(550,news,news) %config /usr/lib/news/bin/parsecontrol
%attr(550,news,news) %config /usr/lib/news/bin/pgpverify
%attr(550,news,news) /usr/lib/news/bin/procbatch
%attr(555,news,news) /usr/lib/news/bin/prunehistory
%attr(555,news,news) /usr/lib/news/bin/pullnews
%attr(550,news,news) %config /usr/lib/news/bin/rc.news
%attr(4550,news,uucp) %config /usr/lib/news/bin/rnews
%attr(555,news,news) /usr/lib/news/bin/rnews.libexec/*
%attr(550,news,news) /usr/lib/news/bin/scanlogs
%attr(550,news,news) /usr/lib/news/bin/scanspool
%attr(550,news,news) /usr/lib/news/bin/send-*
%attr(555,news,news) /usr/lib/news/bin/sendxbatches
%attr(555,news,news) /usr/lib/news/bin/shlock
%attr(555,news,news) /usr/lib/news/bin/shrinkfile
%attr(550,news,news) /usr/lib/news/bin/simpleftp
%attr(550,news,news) /usr/lib/news/bin/sm
%attr(4510,root,news) %config /usr/lib/news/bin/startinnfeed
%attr(550,news,news) /usr/lib/news/bin/tally.control
%attr(550,news,news) /usr/lib/news/bin/writelog

%config(missingok) /usr/lib/news/lib/innreport_inn.pm
%config(missingok) /usr/lib/news/lib/innshellvars
%config(missingok) /usr/lib/news/lib/innshellvars.pl
%config(missingok) /usr/lib/news/lib/innshellvars.tcl

/usr/man/man1/convdate.1.gz
/usr/man/man1/getlist.1.gz
/usr/man/man1/grephistory.1.gz
/usr/man/man1/innconfval.1.gz
/usr/man/man1/innfeed.1.gz
/usr/man/man1/installit.1.gz
/usr/man/man1/nntpget.1.gz
/usr/man/man1/rnews.1.gz
/usr/man/man1/shlock.1.gz
/usr/man/man1/shrinkfile.1.gz
/usr/man/man1/startinnfeed.1.gz
/usr/man/man1/subst.1.gz
/usr/man/man[58]/*

%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/active
%attr(644,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/distributions
%attr(644,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/newsgroups
%attr(644,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/subscriptions
%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/lib/news/active.times
%attr(664,news,news) %config(noreplace) %verify(not size mtime md5) /var/log/news/news.notice
%attr(660,news,news) %config(noreplace) %verify(not size mtime md5) /var/log/news/news.crit
%attr(660,news,news) %config(noreplace) %verify(not size mtime md5) /var/log/news/news.err

%files devel
%defattr(644,root,root,755)
/usr/include/*
/usr/lib/*.a
/usr/man/man3/*

%files -n inews
%defattr(644,root,root,755)

%attr(755,root,root) /usr/bin/inews
%attr(4555,news,news) %config /usr/lib/news/bin/inews
/usr/man/man1/inews.1.gz

%changelog
* Thu Apr 15 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.2-3]
- fixed Group(pl),
- changed Buildroot to /tmp/%{name}-%{version}-root,
- removed man group from man pages,
- removed INSTALL and COPYRIGHT from %doc (copyright statment is in the
  Copyright field),
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
