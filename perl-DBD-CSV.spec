#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	CSV
Summary:	DBD::CSV Perl module
Summary(cs):	Modul DBD::CSV pro Perl
Summary(da):	Perlmodul DBD::CSV
Summary(de):	DBD::CSV Perl Modul
Summary(es):	Módulo de Perl DBD::CSV
Summary(fr):	Module Perl DBD::CSV
Summary(it):	Modulo di Perl DBD::CSV
Summary(ja):	DBD::CSV Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	DBD::CSV ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul DBD::CSV
Summary(pl):	Modu³ Perla DBD::CSV
Summary(pt):	Módulo de Perl DBD::CSV
Summary(pt_BR):	Módulo Perl DBD::CSV
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl DBD::CSV
Summary(sv):	DBD::CSV Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl DBD::CSV
Summary(zh_CN):	DBD::CSV Perl Ä£¿é
Name:		perl-DBD-CSV
Version:	0.2002
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-DBI
BuildRequires:	perl-SQL-Statement
BuildRequires:	perl-Text-CSV_XS
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::CSV - DBI driver for CSV files.

%description -l pl
DBD::CSV - sterownik DBI dla plików CSV.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%doc ChangeLog README
%{perl_sitelib}/DBD/CSV.pm
%{perl_sitelib}/DBD/File.pm
%{_mandir}/man3/*
