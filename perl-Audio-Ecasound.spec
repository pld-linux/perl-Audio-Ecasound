#
# Conditional build:
# _with_tests - perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Ecasound
Summary:	Audio::Ecasound Perl module - bindings to the ecasound control interface
Summary(pl):	Modu³ Perla Audio::Ecasound - dowi±zania do interfejsu ecasound
Name:		perl-Audio-Ecasound
Version:	0.2
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-ecasound-2.1.patch
BuildRequires:	libecasound-devel >= 2.0.1
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio::Ecasound provides perl bindings to the ecasound control
interface of the ecasound program. You can use perl to automate or
interact with ecasound. Ecasound is a software package designed for
multitrack audio processing. It can be used for audio playback,
recording, format conversions, effects processing, mixing and as a
LADSPA plugin host.

%description -l pl
Modu³ Audio::Ecasound udostêpnia dowi±zania do interfejsu
kontroluj±cego program ecasound. Umo¿liwia automatyzacjê czynno¶ci
wykonywanych pod kontrol± tego programu. Ecasound to pakiet s³u¿±cy do
obróbki wielo¶cie¿kowego d¼wiêku. Mo¿e byæ u¿ywany do odtwarzania,
nagrywania, konwersji miêdzy formatami, przepuszczania przez efekty,
miksowania oraz jako baza dla wtyczek LADSPA.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
if [ -x /usr/bin/libecasoundc2-config ]; then
%patch -p1
fi

%build
echo 'y' | perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

# test disabled by default - it hangs
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Audio/Ecasound.pm
%dir %{perl_sitearch}/auto/Audio/Ecasound
%{perl_sitearch}/auto/Audio/Ecasound/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Audio/Ecasound/*.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
