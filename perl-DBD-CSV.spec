#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	CSV
Summary:	DBD::CSV - DBI driver for CSV files
Summary(pl):	DBD::CSV - sterownik DBI dla plik�w CSV
Name:		perl-DBD-CSV
Version:	0.22
Release:	2
Epoch:		1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	365517fb2e0f565b16613eac01046d85
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI >= 1.42
BuildRequires:	perl-SQL-Statement
BuildRequires:	perl-Text-CSV_XS
%endif
Requires:	perl-DBI >= 1.42
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBD::CSV module is yet another driver for the DBI (Database
Independent Interface for Perl). This one is based on the SQL "engine"
SQL::Statement and the abstract DBI driver DBD::File and implements
access to so-called CSV files (Comma separated values). Such files are
mostly used for exporting MS Access and MS Excel data.

%description -l pl
Modu� DBD::CSV jest kolejnym sterownikiem dla DBI (Database Independent
Interface).  Opiera si� na ,,silniku'' SQL -- SQL::Statement, oraz
abstrakcyjnym sterowniku DBD::File (za��czonym w tej dystrybucji).
Implementuje dost�p do tzw. plik�w CSV (Comma Separated Values --
,,warto�ci oddzielone �rednikami'').  Ten format plik�w spotykany jest
najcz�ciej przy eksportowaniu danych z program�w MS Access i MS Excel.

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
%{_mandir}/man3/DBD*.3pm.gz
