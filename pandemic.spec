Name:       pandemic
Version:    0.7.0
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Games/Strategy
Summary:    Operations expert pandemic role
Url:        http://search.cpan.org/dist/%{realname}
Source:     http://www.cpan.org/modules/by-module/Games/Games-Pandemic-%{version}.tar.gz
BuildRequires: perl(Devel::CheckOS)
BuildRequires: perl(Encode)
BuildRequires: perl(English)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(FindBin)
BuildRequires: perl(Geo::Mercator)
BuildRequires: perl(Image::Size)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Locale::TextDomain)
BuildRequires: perl(Module::Util)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::AttributeHelpers)
BuildRequires: perl(MooseX::POE)
BuildRequires: perl(MooseX::SemiAffordanceAccessor)
BuildRequires: perl(MooseX::Singleton)
BuildRequires: perl(MooseX::Traits)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Kernel)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tk)
BuildRequires: perl(Tk::Font)
BuildRequires: perl(Tk::JPEG)
BuildRequires: perl(Tk::PNG)
BuildRequires: perl(Tk::Pane)
BuildRequires: perl(Tk::ToolBar)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(YAML::Tiny)
BuildRequires: x11-server-xvfb
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Pandemic is a cooperative game where the players are united to beat the
game. The goal is to find the cures for various diseases striking cities,
before they propagate too much.

This distribution implements a graphical interface for this game. I
definitely recommend you to buy a 'pandemic' board game and play with
friends, you'll have an exciting time - much more than with this poor
electronic copy.

%prep
%setup -q -n Games-Pandemic-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
xvfb-run make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%{_bindir}/pandemic
%{perl_vendorlib}/Games
%{perl_vendorlib}/LocaleData

