#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Ecasound
Summary:	Audio::Ecasound Perl module - bindings to the ecasound control interface
Summary(pl):	Modu³ Perla Audio::Ecasound - dowi±zania do interfejsu ecasound
Name:		perl-Audio-Ecasound
Version:	0.9
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc3ef490ea84763c055491f494f3eec0
BuildRequires:	ecasound-devel >= 2.2.0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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

%build
echo 'y' | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

# test disabled by default - it hangs
%{?with_tests:%{__make} test}

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
%{perl_vendorarch}/Audio/Ecasound.pm
%dir %{perl_vendorarch}/auto/Audio/Ecasound
%{perl_vendorarch}/auto/Audio/Ecasound/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Ecasound/*.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
