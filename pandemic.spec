%define upstream_name    Games-Pandemic
%define upstream_version 1.092660

Name:       pandemic
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Cooperative pandemic board game
License:    GPL+ or Artistic
Group:      Games/Strategy
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Games/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Convert::Color)
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
BuildRequires: perl(Math::Gradient)
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
BuildRequires: perl(POE::Loop::Tk)
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
BuildRequires: perl-devel

BuildArch: noarch

# bug #56809: prereq not automatically found
Requires: perl(POE::Loop::Tk)

%description
Pandemic is a cooperative game where the players are united to beat the
game. The goal is to find the cures for various diseases striking cities,
before they propagate too much.

This distribution implements a graphical interface for this game. I
definitely recommend you to buy a 'pandemic' board game and play with
friends, you'll have an exciting time - much more than with this poor
electronic copy.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#xvfb-run make test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%{_bindir}/pandemic
%{perl_vendorlib}/Games
%{perl_vendorlib}/LocaleData


%changelog
* Mon Jan 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1.92.660-2mdv2010.1
+ Revision: 486105
- fix #56809: missing requires:

* Thu Sep 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.92.660-1mdv2010.0
+ Revision: 448257
- update to 1.092660

* Wed Sep 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1.92.640-1mdv2010.0
+ Revision: 447821
- update to 1.092640

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 437200
- update to 1.000000

  + Michael Scherer <misc@mandriva.org>
    - fix Url tag, as found out by neoclust

* Mon Aug 31 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.0-1mdv2010.0
+ Revision: 422838
- new version
- desactivate tests, xvfb segfaults

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 420194
- run tests through xvfb
- import pandemic


* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.0-1mdv2010.0
- initial mdv release
