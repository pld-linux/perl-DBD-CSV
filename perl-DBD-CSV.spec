%include	/usr/lib/rpm/macros.perl
Summary:	DBD-CSV perl module
Summary(pl):	Modu³ perla DBD-CSV
Name:		perl-DBD-CSV
Version:	0.1022
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/DBD-CSV-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-DBI
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	perl-SQL-Statement
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
DBD-CSV - DBI driver for CSV files.

%description -l pl
DBD-CSV - sterownik DBI dla plików CSV.

%prep
%setup -q -n DBD-CSV-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/DBD/CSV
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Bundle/DBD/CSV.pm
%{perl_sitelib}/DBD/CSV.pm
%{perl_sitelib}/DBD/File.pm

%{perl_sitearch}/auto/DBD/CSV

%{_mandir}/man3/*
