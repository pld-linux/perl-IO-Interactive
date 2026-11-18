#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Interactive
Summary:	IO::Interactive - Utilities for interactive I/O
Name:		perl-IO-Interactive
Version:	1.027
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/B/BR/BRIANDFOY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	490b2d3375c5a4e49febd71ffe296d3d
URL:		http://search.cpan.org/dist/IO-Interactive/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides three utility subroutines that make it easier to
develop interactive applications...



%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/IO/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
