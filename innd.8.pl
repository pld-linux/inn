.\" $Revision$
.TH INND 8
.SH NAZWA
innd, inndstart \- InterNetNews daemon
.SH SK�ADNIA
.B innd
[
.B \-a
]
[
.BI \-c " dni"
]
[
.B \-C
]
[
.B \-d
]
[
.B \-f
]
[
.BI \-H " licznik"
]
[
.BI \-i " licznik"
]
[
.BI \-I "adres_IP"
]
[
.BI \-l " rozmiar"
]
[
.B \-L
]
[
.BI \-m " tryb"
]
[
.BI \-n " flaga"
]
[
.BI \-o " licznik"
]
[
.BI \-p "fd_des"
]
[
.BI \-P "port"
]
[
.B \-r
]
[
.B \-s
]
[
.BI \-t " op�nienie"
]
[
.BI \-T " licznik"
]
[
.B \-u
]
[
.BI \-X " sekundy"
]
[
.B \-Z
]

.B inndstart
[
.B flagi
]
.SH OPIS
.IR Innd ,
kt�ry jest demonem news (InterNetNews), obs�uguje wszystkie nadchodz�ce
feedy. Najpierw wczytuje do pami�ci pliki
.IR active (5),
.IR newsfeeds (5)
i
.IR incoming.conf (5).
Potem otwiera port NNTP do odbierania artyku��w ze zdalnych stacji (zobacz
opcj� ``\fB\-p\fP''). Je�li w include/config.h zdefiniowano
.IR HAVE_UNIX_DOMAIN_SOCKETS ,
to do odbioru artyku��w od lokalnych proces�w, takich jak 
.IR nnrpd (8)
i
.IR rnews (1)
otwierane jest gzniazdo strumieniowe dziedziny Uniksowej, a dla
.IR ctlinnd (8)
odwierane jest analogiczne gniazdo datagramowe.
Gdy makro to nie jest zdefiniowane, u�ywane s� ��cza nazwane.
.IR Ctlinnd (8)
wykorzystywany jest do kierowania serwer na wykonywanie okre�lonych akcji.
Otwiera r�wnie� baz�
.IR history (5)
i dwa pliki raportowe, zast�puj�ce jego standardowe wyj�cie i wyj�cie b��du.
.PP
Po otwarciu wszystkich plik�w i gniazd,
.I innd
oczekuje na po��czenia i dane na swoich portach, u�ywaj�c do tego
.IR select (2)
i nieblokuj�cego I/O.
Je�li nie ma dost�pnych danych, to wypr�ni od swoje wewn�trzrdzeniowe
struktury danych. Domy�lna liczba sekund op�nienia przed wypr�nieniem jest
ustawiana jako
.I <DEFAULT_TIMEOUT w config.data>
(zwykle
.\" =()<.IR @<typDEFAULT_TIMEOUT>@ ) >()=
.IR 300 ) 
sekund.
.PP
Je�li 
.I innd
otrzyma b��d ENOSPC (zobacz
.IR intro (2))
podczas zapisu pliku
.IR active ,
pliku article, lub bazy historii, to wy�le sobie komend� ``throttle''.
Stanie si� to r�wnie� je�li otrzyma zbyt wiele b��d�w I/O podczas pr�by
zapisu do jakiego� pliku.
.SH OPCJE
.TP
.B \-a
Domy�lnie, je�li host nie jest wymieniony w pliku
.I incoming.conf
to po��czenie jest przekazywane do
.IR nnrpd .
Po u�yciu tej flagi dowolny host mo�e si� pod��czy� i przesy�a� artyku�y.
.TP
.B \-c
.I innd
odrzuca stare artyku�y. Zasadniczo zachowanie to mo�e by� sterowane przez
baz� historii, lecz czasem stacja wyrzuca w sie� paczk� bardzo starych
artyku��w. Flaga ``\fB\c\fP'' okre�la odci�cie. Na przyk�ad ``\fB\-c21\fP''
odrzuca wszelkie artyku�y, wys�ane dawniej ni� 21 dni temu. Warto�� zerowa
powstrzymuje ten test. Domy�ln� warto�ci� jest 14 dni, lecz mo�na to zmieni�
opcj� ``artcutoff'' w
.IR inn.conf (5)
.TP
.B \-C
Je�li u�yta jest flaga ``\fB\-C\fP'', to
.I innd
przyjmie i przepropaguje lecz nie przetwarza wiadomo�ci anulowania i
powstrzymania. Jest to przeznaczone dla stacji, w kt�rych nadu�ywane s�
anulowania i kt�re wybieraj� mechanizm z lepsz� autoryzacj�.
.TP
.B "\-d \-f"
.I Innd
normalnie przechodzi w t�o, ustawia standardowe wyj�cia na pliki raportowe i
od��cza si� od terminala. Po u�yciu flagi ``\fB\-d\fP'' serwer tego nie
robi, a po u�yciu flagi ``\fB\-f\fP'', serwer pozostaje na pierwszym planie.
.TP
.B "\-H \-T \-X"
Flagi ``\fB\-H\fP'', ``\fB\-T\fP'' i ``\fB\-X\fP'' steruj� liczb� po��cze�
dozwolonych na minut�. Ma to w za�o�eniach dzia�a� jako ochrona serwera
przed czytnikami, kt�re wykonuj� w ci�gu minuty zbyt wiele po��cze� z
serwerem. Zazwyczaj nie u�ywa si� tego, chyba �e rzeczywi�cie pojawia si�
jaki� problem.
Tablica u�ywana do tych sprawdze� jest ograniczona do 128 wpis�w i jest
u�ywana jako pier�cie� (ring). Rozmiar zosta� wybrany do u�atwienia
obliczania indeksu i do upewnienia si�, �e nie zabraknie ci miejsca.
Praktycznie wydaje si� w�tpliwe, �eby� wykorzysta� nawet po�ow� tablicy
naraz.
.IP
Flaga ``\fB\-H\fP'' ogranicza liczb� razy, do kt�rej host mo�e si� po��czy�
z serwerem podczas ``\fB\-X\fP'' sekund. Domy�lnie 2.
.IP
Flaga ``\fB\-T\fP'' ogranicza ca�kowit� liczb� nadchodz�cych po��cze� innda
w okresie ``\fB\-X\fP'' sekund. Maksymaln� warto�ci� jest 128. Domy�ln� 60.
.IP
Flaga ``\fB\-X\fP'' ustawia liczb� sekund, u�ywan� przez  ``\fB\-H\fP'' i
``\fB\-T\fP''. Warto�� zerowa wy��cza sprawdzanie. Domy�lnie jest 0.
.TP
.B \-i
Flaga ``\fB\-i\fP'' ogranicza liczb� nadchodz�cych po��cze� NNTP. Warto��
zerowa wy��cza to sprawdzenie. Domy�ln� warto�ci�, je�li w \fIinn.conf\fR(5)
nie podano opcji ``maxconnections'' jest 50.
Wymieniona opcja jest zast�powana warto�ci� tej opcji.
.TP
.B \-I
Opcja ta umo�liwia wi�zanie innda do podanego adresu interfejsu IP. Adres IP
musi by� w postaci kropkowej czw�rki liczb (nnn.nnn.nnn.nnn). Zobacz te�
opcj� ``bindaddress'' w
.IR inn.conf (5).
.TP
.B \-l
Flaga ``\fB\-l\fP'' ogranicza rozmiar artyku�u. Po u�yciu tej flagi,
wszystkie artyku�y wi�ksze ni�
.I rozmiar
bajt�w b�d� odrzucane. Domy�ln� warto�ci� jest 1000000L bajt�w. Sprawdzanie
mo�na wy��czy�, u�ywaj�c warto�ci zerowej.
.TP
.B \-L
Flaga ``\fB\-L\fP'' powoduje, �e
.I innd
nie tworzy dowi�za� do crosspostowanych artyku��w. Stacja typu
``feed-only'' mo�e tego u�y� do zwi�kszenia wydajno�ci. Mo�na to te�
po��czy� z feedem kana�owym do programu
.IR crosspost (8)
i przerzuci� zadanie tworzenia dowi�za� poza p�tl� przetwarzania innda.
.TP
.B \-m
Flaga ``\fB\-m\fP'' s�u�y do uruchamiania serwera w zatrzymanym lub
st�umionym stanie (zobacz
.IR ctlinnd (8)).
Argument rozpoczyna si� pojedyncz� liter�:
.IR g ,
.IR p
lub
.IR t ,
wskazuj�ce na ``go'' (startuj), ``pause'' (zatrzymaj) lub ``throttle''
(st�um).
.TP
.B \-n
Flaga ``\-n'' okre�la czy pauzowanie lub st�umienie serwera powinno r�wnie�
wy��czy� przysz�e procesy czytnikowe. Warto�� ``\fBy\fP'' powoduje, �e
czytniki zachowuj� si� jak serwer, a warto�� ``\fBn\fP'' umo�liwia czytanie
nawet gdy serwer nie pracuje.
Domy�lnie zezwala si� na czytanie, a zmieni� mo�na to opcj�
``readerswhenstopped'' z
.IR inn.conf (5).
.TP
.B \-o
Flaga ``\fB\-o\fP'' s�u�y ograniczaniu ilo�ci plik�w, kt�re s� utrzymywane
otwarte dla wychodz�cych feed�w plikowych. Domy�ln� warto�ci� jest liczba
dost�pnych deskryptor�w minus cz�� zarezerwowana do u�ytku wewn�trznego.
.TP
.B \-p
Po u�yciu flagi ``\fB\-p\fP'' przyjmuje si�, �e port NNTP jest otwierany na
podanym deskryptorze. (Je�li u�yta jest ta flaga, to
.I innd
zak�ada, �e pracuje z w�a�ciwymi uprawnieniami i nie b�dzie wo�a�
.IR chown (2)
na �adnych z tworzonych plik�w lub katalog�w.)
.TP
.B \-P
Je�li u�yta jest flaga ``\fB\-P\fP'', to podany port jest u�ywany do
nas�uchiwania po��cze�.
.I innd
musi mie� wystarczaj�ce uprawnienia startowe by otworzy� podany port.
.TP
.B \-r
Je�li u�yta jest flaga ``\fB\-r\fP'', serwer przenumeruje plik
.I active
zupe�nie tak, jak po wys�aniu komendy ``renumber''.
.TP
.B \-s
Je�li u�yta jest flaga ``\fB\-s\fP'', to
.I innd
nic nie b�dzie robi�, lecz tylko sprawdzi sk�adni� pliku
.IR newsfeeds .
Je�li b�d� tam b��dy, to zg�osi kod b��du; rzeczywiste b��dy b�d� natomiast
zg�oszone w
.IR syslog (3).
.TP
.B \-t
Zmienia czas op�nienia przed wypr�nieniem do
.IR timeout 
sekund.
.TP
.B \-u
Raporty s� normalnie buforowane; flaga ta wy��cza to zachowanie.
.TP
.B "\-Z"
Flaga ``\fB\-Z\fP'' wy��cza strumieniowanie, wi�c
.I innd
nie przyjmie `mode stream' i innych polece� strumieniowych.
.PP
.I Inndstart
jest ma�ym programem typu front-end, kt�ry otwiera port NNTP, ustawia uid i
gid na opiekuna news, a nast�pnie uruchamia demona
.I innd
z flag� ``\fB\-p\fP'' i minimalnym bezpiecznym �rodowiskiem.
Jest to ma�y front-end dla stacji, kt�ra nie chce uruchamia� 
.I innd
z uprawnieniami roota.
.SH "KOMUNIKATY STERUJ�CE"
Artyku�y przychodz�ce, maj�ce nag��wek Control, lub nag��wek Subject, kt�ry
rozpoczyna si� pi�cioma znakami \&``cmsg\ '',  s� nazywane
.IR "komunikatami steruj�cymi" .
Poza komunikatem anulowania, s� one zaimplementowane przez zewn�trzne
programy w katalogu
.I <pathcontrol w inn.conf>
o ile
.I <usecontrolchan w inn.conf>
jest ustawione na ``false''. (Komunikaty anulowania (cancel) od�wie�aj� baz�
historii, wi�c musz� by� obs�ugiwane wewn�trznie; koszt synchronizowania,
blokowania i odblokowywania by�by zbyt wysoki przy odbiorze wielu takich
komunikat�w.)
.PP
Gdy nadchodzi komunikat steruj�cy, pierwsze s�owo tekstu jest konwertowane
na ma�e litery i jest u�ywane jako nazwa uruchamianego programu. Je�li
program nie istnieje, wywo�ywany jest domy�lny program, okre�lony przez
.IR "<pathcontrol w inn.conf>/default" .
.PP
Wszystkie programy steruj�ce s� wywo�ywane z czterema parametrami. Pierwszym
jest adres nadawcy komunikatu; jest to pobierane z nag��wka Sender. Je�li
nag��wek ten jest pusty, to dane s� pobierane z nag��wka From. Nast�pnym
parametrem jest adres zwrotny replik; pobierany z nag��wka Reply-To.
Je�li nag��wek ten jest pusty, u�yty zostanie adres nadawcy.
Trzecim parametrem b�dzie nazwa pliku, w kt�rym znajduje si� artyku�
wzgl�dem katalogu sk�adowego news.
Czwartym parametrem jest host, kt�ry wys�a� artyku�. Jest to odczytywane z
linii Path.
.PP
Je�li
.I <usecontrolchan w inn.conf> 
jest ustawione na ``true'', to �aden komunikat steruj�cy nie b�dzie
przetwarzany przez program zewn�trzny, forkowany przez innda. Zamiast tego,
b�dzie przetwarzany przez skrypt
.IR controlchan ,
kt�ry jest wywo�ywany jako program kana�owy innda. Nie musisz do u�ywania
tego skryptu konfigurowa�
.IR newsfeeds (5).
Przetwarzanie z u�yciem
.I controlchan
mo�e zredukowa� nadmierne obci��enie, je�li zbyt wiele komunikat�w
steruj�cych pojawia si� naraz.
.PP
Dystrybucja komunikatu steruj�cego jest odmienna od dystrybucji
standardowych artyku��w.
.PP
Komunikaty steruj�ce normalnie wpadaj� do grupy dyskusyjnej
.IR control .
Mog� one by� zapisywane w podgrupach, lecz w oparciu o polecenie komunikatu
steruj�cego.
Na przyk�ad komunikat newgroup mo�e by� zapisany w grupie
.I control.newgroup
lub w og�lnym
.IR control ,
je�li specjalizowana podgrupa nie istnieje.
.PP
Stacje mog� jawnie udost�pnia� grup� ``control'' w ich listach zapisowych,
lecz zwykle lepiej jest j� wy��czy�. Je�li komunikat steruj�cy jest wysy�any
na grup�, kt�rej nazwa ko�czy si� czterema znakami ``.ctl'', to przyrostek
jest obcinany, a to co pozostanie jest u�ywane jako nazwa grupy.
Na przyk�ad komunikat anuluj�cy, wys�any na ``news.admin.ctl'' zostanie
przes�any do wszystkich stacji zapisanych na grupy ``control'' lub
``news.admin''.
.PP
Je�li
.I <mergetogroups w inn.conf>
jest ustawione na ``true'', to gdy artyku� jest wysy�any na grup�, kt�ra
rozpoczyna si� trzema literami ``to.'', to zostanie potraktowany specjalnie
je�li grupa ta nie istnieje w pliku
.IR active :
artuku� jest sk�adowany do grupy ``to'' i jest wysy�any do pierwszej stacji,
nazwanej po przedrostku. Na przyk�ad, wysy�anie do ``to.uunet'' zostanie
z�o�one do ``to'' i przes�ane do stacji ``uunet''.
file:
.SH "RӯNICE PROTOKO�U"
.I Innd
implementuje komendy NNTP zdefiniowane w RFC 977 z nast�puj�cymi
odst�pstwami:
.IP 1.
Za
\&``\fIlist\fP''
mo�e wyst�powa� dodatkowo argument
\&``\fIactive\fP'',
\&``\fIactive.times\fP'',
\&``\fInewsgroups\fP''
lub
\&``\fIsubscription\fP''.
Jest to popularne rozszerzenie, lecz nie w pe�ni obs�ugiwane; zobacz
.IR nnrpd (8).
.IP 2.
Zaimplementowane s� komendy
\&``\fIauthinfo user\fP''
oraz
\&``\fIauthinfo pass\fP''.
Zobacz draft-barber-nntp-imp-07.txt dla dalszych szczeg��w.
.IP 3.
Udost�pniona jest nowa komenda,
\&``\fImode reader\fP''.
Komenda ta powoduje, �e serwer przekazuje po��czenie do
.IR nnrpd .
Komenda
\&``\fImode query\fP''
przeznaczona jest dla przysz�ych zastosowa� i obecnie jest traktowana tak
samo.
.IP 4.
Udost�pnione s� komendy wspieraj�ce transfer strumieniowy:
\&``\fIcheck messageid\fP'' i ``\fItakethis messageid\fP''.
.IP 5.
Udost�pniona jest komenda transferu wsadowego ``\fIxbatch
liczba-bajt�w\fP''. Komenda ta odczyta \fIliczb�-bajt�w\fP bajt�w i zapisze
je dla dalszego przetwarzania przez rnews(1) (kt�ry nale�y uruchomi�
oddzielnie). Obejrzyj programy innxbatch i sendxbatches.sh.
.IP 6.
Pozosta�ymi zaimplementowanymi komendami s�
\&``\fIhead\fP'' ,
\&``\fIhelp\fP'' ,
\&``\fIihave\fP'' ,
\&``\fIquit\fP''
oraz
\&``\fIstat\fP''.
.SH "MODYFIKACJE NAG��WK�W"
.I Innd
modyfikuje tak ma�o nag��wk�w, jak ma�o si� da, lecz m�g�by by� lepszy.
.PP
Oto lista nag��wk�w, kt�re, je�li istniej�, s� usuwane:
.RS
.nf
Date-Received
Posted
Posting-Version
Received
Relay-Version
.fi
.RE
Puste nag��wki oraz nag��wki, sk�adaj�ce si� z bia�ych spacji r�wnie� s�
opuszczane.
.PP
Do nag��wka Path doklejana jest nazwa lokalnej stacji 
(okre�lanej przez warto�� ``pathhost'' w
.IR inn.conf (5))
i wyrzyknik (je�li nazwa pierwszej stacji nag��wka r�ni si� od lokalnej).
.PP
Nag��wek Xref jest usuwany i tworzony jest nowy.
.PP
W przypadku nieobecno�ci, nag��wek Lines jest dodawany.
.PP
.I Innd
nie przepisuje nieprawid�owych nag��wk�w. Na przyk�ad nie b�dzie zmienia�
nieprawid�owego nag��wka Lines, ale odrzuci artyku�.
.SH RAPORTOWANIE
.I Innd
raportuje wszystkie nadchodz�ce artyku�y do pliku raportowego. Jest to plik
tekstowy o zmiennej ilo�ci rozdzielanych spacjami p�l o jednym z
nast�puj�cych format�w:
.RS
.nf
mon dd hh:mm:ss.mmm + feed <Message-ID> stacja...
mon dd hh:mm:ss.mmm j feed <Message-ID> stacja...
mon dd hh:mm:ss.mmm c feed <Message-ID> stacja...
mon dd hh:mm:ss.mmm - feed <Message-ID> pow�d...
.fi
.RE
.PP
Po polu Message-ID mo�e by� r�wnie� pole nazwy hosta i rozmiaru, zale�nie od
opcji ``nntplinklog'' i ``logsize'' z
.IR inn.conf (5).
.PP
Pierwsze trzy pola s� polami daty i czasu w rozdzielczo�ci milisekundowej.
Pi�te pole jest stacj�, kt�ra wys�a�a artyku� (odczytywane z nag��wka Path).
Sz�ste pole jest identyfikatorem artyku�u; je�li informacja jest
niedost�pna, pojawi si� w jej miejscu pytajnik.
.PP
Czwarte pole okre�la czy artyku� zosta� przyj�ty czy nie. Je�li jest tam
znak plus, to zosta� przyj�ty. Je�li ``j'', to zosta� przyj�ty, lecz
wszystkie grupy maj� w swoich rekordach
.I active
``j'', wi�c artyku� zosta� z�o�ony do grupy ``junk''.
Je�li w polu pojawi�a si� litera ``c'', to przed pojawieniem si�
oryginalnego artyku�u odebrany zosta� komunikat anuluj�cy.
We wszystkich tych przypadkach artyku� zosta� przyj�ty i pole ``stacja...''
zawiera rozdzielon� spacjami list� stacji, do kt�rych artyku� jest
przesy�any.
.PP
Je�li czwarte pole zawiera znak minusa, o artyku� zosta� odrzucony. Powodami
odrzucenia mog� by�:
.RS
.nf
"%s" header too long (za d�ugi nag��wek)
"%s" wants to cancel <%s> by "%s" ("%s" chce anulowa� <%c> poprzez "%s")
Article exceeds local limit of %s bytes (Artyku� przekracza lokalny 
                                         limit %s bajt�w)
Article posted in the future -- "%s" (Artyku� wys�any w przysz�o�ci -- "%s")
Bad "%s" header (Z�y nag��wek "%s")
Can't write history (Nie mog� zapisa� historii)
Duplicate (Duplikat)
Duplicate "%s" header (Zduplikowany nag��wek "%s")
EOF in headers (EOF w nag��wkach)
Linecount %s != %s +- %s (Liczba linii %s != %s +- %s)
Missing %s header (Brak nag��wka %s)
No body (Brak cia�a)
No colon-space in "%s" header (Brak dwukropka-spacji w nag��wku "%s")
No space (Brak spacji (albo miejsca???))
Space before colon in "%s" header (Spacja przed dwukropkiem w nag��wku "%s")
Too old -- "%s" (Za stare -- "%s")
Unapproved for "%s" (Niezatwierdzone dla "%s")
Unwanted newsgroup "%s" (Niechciana grupa dyskusyjna "%s")
Unwanted distribution "%s" (Niechciana dystrybucja "%s")
Whitespace in "Newsgroups" header -- "%s" (Bia�a spacja w nag��wku
                                           "Newsgroups" -- "%s")
.fi
.RE
Gdzie ``%s'' jest podmieniane przez konretniejsze informacje.
.PP
Zauwa�, �e je�li artyku� jest przyj�ty i <wanttrash w inn.conf> jest
ustawione na ``ues'' i �adna z grup nie jest odpowiednia, to zostanie
zraportowany w dw�ch liniach: w linii ``j'' i ``\-''.
.PP
.I Innd
zg�asza te� obszerne raporty poprzez
.IR syslog a.
Pierwsze s�owo komunikatu raportowego b�dzie: nazw� stacji, je�li wpis jest
dla niej specyficzny (np. komunikat ``connected''); s�owem ``SERVER'', je�li
komunikat jest zwi�zany z serwerem, np. gdy pojawi si� b��d odczystu.
.PP
Je�li drugim s�owem s� cztery litery ``cant'', to zg�aszany jest b��d.
W tym przypadku nast�pne dwa s�owa og�lnie nazywaj� wywo�anie systemowe lub
funkcj� biblioteczn�, kt�ra si� nie powiod�a oraz obiekt, wok� kt�rego
wykonywane by�y dzia�ania. Reszta linii mo�e zawiera� inne informacje.
.PP
W innych przypadkach, drugie s�owa okre�la rodzaj zmiany, a reszta linii
u�ci�la t� informacj�. S�owo ``internal'' og�lnie oznacza wewn�trzny b��d
logiczny.
.SH SYGNA�Y
.I Innd
przechwytuje sygna�y SIGTERM i SIGDANGER i wy��cza si� po nich. Je�li u�yta
jest flaga ``-d'', przechwytywany b�dzie r�wnie� SIGINT i b�dzie dzia�a�
analogicznie.
.PP
.I Innd
przechwytuje sygna� SIGUSR1 i odtwarza kana� steruj�cy, wykorzystywany
normalnie dla
.IR ctlinnd (8).
.SH HISTORIA
Napisane przez Richa $alza <rsalz@uunet.uu.net> dla InterNetNews.
.de R$
Jest to rewizja \\$3, z daty \\$4.
..
.R$ $Id$
.SH "ZOBACZ TAK�E"
active(5),
ctlinnd(8),
crosspost(8),
dbz(3),
history(5),
incoming.conf(5),
inn.conf(5),
newsfeeds(5),
nnrpd(8),
rnews(1),
syslog(8).
