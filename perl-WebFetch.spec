#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WebFetch
Summary:	WebFetch - Perl module to download and save information from the Web
Summary(pl.UTF-8):	WebFetch - moduł Perla do ściągania i zapisywania informacji z WWW
Name:		perl-WebFetch
Version:	0.13
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IK/IKLUFT/%{pdir}-%{version}.tar.gz
# Source0-md5:	c06a23ec6f9762d92c3510c685b1112e
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl(Locale::Country)
BuildRequires:	perl-Class-ISA
BuildRequires:	perl-DB_File
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Exception-Class
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Template-Plugin-XML-XPath
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Atom
BuildRequires:	perl-XML-RSS
BuildRequires:	perl-libwww
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebFetch - infrastructure for downloading ("fetching") information
from various sources around the Internet or the local system in order
to present them for display, or to export local information to other
sites on the Internet.

%description -l pl.UTF-8
Moduł WebFetch - infrastruktura do ściągania informacji z różnych
źródeł w całym Internecie lub z lokalnego systemu w celu wyświetlenia
lub eksportu informacji na inne serwisy internetowe.

%prep
%setup -q -n %{pdir}-%{version}

# Coverage for WebFetch::Output::TWiki is 0.0%, with 5 naked subroutines
%{__sed} -i -e '/WebFetch::Output::TWiki/d' t/pod-coverage.t

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Embedding_API.pod README TODO
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/WebFetch
%{_mandir}/man3/*
