%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	CSV
Summary:	DBD-CSV perl module
Summary(pl):	Modu³ perla DBD-CSV
Name:		perl-DBD-CSV
Version:	0.1027
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-DBI
BuildRequires:	perl-Text-CSV_XS
BuildRequires:	perl-SQL-Statement
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD-CSV - DBI driver for CSV files.

%description -l pl
DBD-CSV - sterownik DBI dla plików CSV.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%{perl_sitelib}/DBD/CSV.pm
%{perl_sitelib}/DBD/File.pm
%{_mandir}/man3/DBD*
