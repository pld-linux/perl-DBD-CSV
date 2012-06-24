%include	/usr/lib/rpm/macros.perl
Summary:	DBD-CSV perl module
Summary(pl):	Modu� perla DBD-CSV
Name:		perl-DBD-CSV
Version:	0.1025
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/DBD-CSV-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	perl-SQL-Statement
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD-CSV - DBI driver for CSV files.

%description -l pl
DBD-CSV - sterownik DBI dla plik�w CSV.

%prep
%setup -q -n DBD-CSV-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Bundle/DBD/CSV.pm
%{perl_sitelib}/DBD/CSV.pm
%{perl_sitelib}/DBD/File.pm
%{_mandir}/man3/*
