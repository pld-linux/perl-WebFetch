#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	WebFetch
Summary:	WebFetch - Perl module to download and save information from the Web
Summary(pl):	WebFetch - modu³ Perla do ¶ci±gania i zapisywania informacji z WWW
Name:		perl-WebFetch
Version:	0.10
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-authors/id/I/IK/IKLUFT/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(Locale::Country)
BuildRequires:	perl-libwww
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Parser
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebFetch - infrastructure for downloading ("fetching") information
from various sources around the Internet or the local system in order
to present them for display, or to export local information to other
sites on the Internet.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/%{pdir}
#%{perl_sitelib}/auto/%{pdir}
%{_mandir}/man3/*
