.\" {PTM/PB/0.1/20-06-1999/"Pobierz listê z serwera NNTP"}
.\" $Revision$
.TH GETLIST 1
.SH NAZWA
getlist \- pobierz listê z serwera NNTP
.SH SK£ADNIA
.I getlist
[
.BI \-h " host"
]
[
.I lista
[
.I wzorzec
[
.I typy
]
]
]
.SH OPIS
Program
.I getlist
uzyskuje listê z serwera NNTP i wysy³a j± na standardowe wyj¶cie.
.PP
Parametr
.B lista
mo¿e byæ jednym z
.IR active ,
.IR active.times ,
.IR distributions ,
lub
.IR newsgroups .
Argumenty te ¿±daj± odpowiednio plików
.IR active (5),
.IR active.times ,
.\" =()<.IR @<_PATH_NEWSLIB>@/distributions ,>()=
.IR /etc/news/distributions ,
lub
.\" =()<.I @<_PATH_NEWSLIB>@/newsgroups>()=
.IR /etc/news/newsgroups .
.PP
Je¶li u¿yta zostanie flaga ,,\-h'', program pod³±cza siê do serwera na
podanym ho¶cie. Domy¶lnie jest to serwer podany w pliku
.IR inn.conf (5).
.PP
Je¶li parametrem
.I listy
jest
.IR active ,
to do ograniczania wyj¶cia mog± zostaæ u¿yte parametry
.I wzorzec
i
.I typy .
Je¶li podano
.IR wzorzec ,
wypisywane s± tylko te linie grup, które odpowiadaj± mu wed³ug
.IR wildmat (3).
Je¶li podano
.IR typy ,
to wy¶wietlane s± tylko te linie, których czwarte pole zaczyna siê od znaku
wymienionego w
.IR typy .
.PP
Na przyk³ad nastêpuj±ce polecenie da nam jednolinijkowe opisy wszystkich grup
dyskusyjnych UUNET-u:
.RS
getlist -h news.uu.net newsgroups
.RE
.PP
Poni¿sze polecenie wypisuje wszystkie grupy, w których dozwolone jest
lokalne wysy³anie artyku³ów, grupy, które s± moderowane lub aliasowane
.RS
getlist active '*' ym=
.RE
.PP
Zauwa¿, ¿e listowanie plików innych ni¿ plik active to tylko popularne
rozszerzenie protoko³u NNTP i nie wszêdzie musi byæ dostêpne.
.SH HISTORIA
Napisane przez Landona Curta Nolla <chongo@toad.com> dla InterNetNews.
.de R$
Jest to wersja \\$3, z dnia \\$4.
..
.SH "ZOBACZ TAK¯E"
active(5), nnrpd(8), wildmat(3).
