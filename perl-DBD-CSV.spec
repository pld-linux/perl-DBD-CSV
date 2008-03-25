#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	CSV
Summary:	DBD::CSV - DBI driver for CSV files
Summary(pl.UTF-8):	DBD::CSV - sterownik DBI dla plików CSV
Name:		perl-DBD-CSV
Version:	0.22
Release:	3
Epoch:		1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	365517fb2e0f565b16613eac01046d85
URL:		http://search.cpan.org/dist/DBD-CSV/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI >= 1.42
BuildRequires:	perl-SQL-Statement
BuildRequires:	perl-Text-CSV_XS
%endif
Requires:	perl-DBI >= 1.42
Requires:	perl-SQL-Statement
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBD::CSV module is yet another driver for the DBI (Database
Independent Interface for Perl). This one is based on the SQL "engine"
SQL::Statement and the abstract DBI driver DBD::File and implements
access to so-called CSV files (Comma separated values). Such files are
mostly used for exporting MS Access and MS Excel data.

%description -l pl.UTF-8
Moduł DBD::CSV jest kolejnym sterownikiem dla DBI (Database Independent
Interface).  Opiera się na ,,silniku'' SQL -- SQL::Statement, oraz
abstrakcyjnym sterowniku DBD::File (załączonym w tej dystrybucji).
Implementuje dostęp do tzw. plików CSV (Comma Separated Values --
,,wartości oddzielone średnikami'').  Ten format plików spotykany jest
najczęściej przy eksportowaniu danych z programów MS Access i MS Excel.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc ChangeLog README
%{perl_vendorlib}/DBD/CSV.pm
%{_mandir}/man3/DBD*.3pm*
