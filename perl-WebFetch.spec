#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WebFetch
Summary:	WebFetch - Perl module to download and save information from the Web
Summary(pl):	WebFetch - modu³ Perla do ¶ci±gania i zapisywania informacji z WWW
Name:		perl-WebFetch
Version:	0.10
Release:	5
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IK/IKLUFT/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(Locale::Country)
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww
%endif
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebFetch - infrastructure for downloading ("fetching") information
from various sources around the Internet or the local system in order
to present them for display, or to export local information to other
sites on the Internet.

%description -l pl
Modu³ WebFetch - infrastruktura do ¶ci±gania informacji z ró¿nych
¼róde³ w ca³ym Internecie lub z lokalnego systemu w celu wy¶wietlenia
lub eksportu informacji na inne serwisy internetowe.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/*.pm
%{perl_sitelib}/WebFetch
# empty autosplit.ix files
%{perl_sitelib}/auto/WebFetch
%{_mandir}/man3/*
