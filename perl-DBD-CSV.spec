#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	CSV
Summary:	DBD::CSV - DBI driver for CSV files
Summary(pl):	DBD::CSV - sterownik DBI dla plików CSV
Name:		perl-DBD-CSV
Version:	0.2002
Release:	4
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a98138aee1c94747d86494ceb343c2b
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
BuildRequires:	perl-SQL-Statement
BuildRequires:	perl-Text-CSV_XS
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBD::CSV module is yet another driver for the DBI (Database
Independent Interface for Perl). This one is based on the SQL "engine"
SQL::Statement and the abstract DBI driver DBD::File and implements
access to so-called CSV files (Comma separated values). Such files are
mostly used for exporting MS Access and MS Excel data.

%description -l pl
Modu³ DBD::CSV jest kolejnym sterownikiem dla DBI (Database Independent
Interface).  Opiera siê na ,,silniku'' SQL -- SQL::Statement, oraz
abstrakcyjnym sterowniku DBD::File (za³±czonym w tej dystrybucji).
Implementuje dostêp do tzw. plików CSV (Comma Separated Values --
,,warto¶ci oddzielone ¶rednikami'').  Ten format plików spotykany jest
najczê¶ciej przy eksportowaniu danych z programów MS Access i MS Excel.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/DBD/CSV.pm
%{perl_vendorlib}/DBD/File.pm
%{_mandir}/man3/DBD*
