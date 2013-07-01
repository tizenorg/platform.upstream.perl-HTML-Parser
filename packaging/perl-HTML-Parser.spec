Name:           perl-HTML-Parser
Version:        3.69
Release:        0
License:        GPL-2.0+ or Artistic
Summary:        Perl module for parsing HTML
Url:            http://search.cpan.org/dist/HTML-Parser/
Group:          Development/Libraries
Source0:        HTML-Parser-%{version}.tar.gz
Source1001: 	perl-HTML-Parser.manifest
BuildRequires:  perl(HTML::Tagset) >= 3.03
Requires:       perl(HTML::Tagset) >= 3.03

%description
The HTML-Parser module for perl to parse and extract information from
HTML documents, including the HTML::Entities, HTML::HeadParser,
HTML::LinkExtor, HTML::PullParser, and HTML::TokeParser modules.

%prep
%setup -q -n HTML-Parser-%{version}
cp %{SOURCE1001} .

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%docs_package

%files -f %{name}.files
