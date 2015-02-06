Name:		unsermake
Version:	0.4
Release:	6
Summary:	Buildsystem utility to supersed auto* tools
Summary(pt_BR):	Utilitário para sobreposição das ferramentas auto* em buildsystems
Group:		Development/Other
Group(pt_BR):	Utilitários
Group(es):	Utilitarios
License:	GPL
URL:		http://www.kde.org/
Source0:	%{name}-%{version}.tar.bz2
Source1:	unsermake.sh
Requires:	python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Buildsystem utility to supersed auto* tools

%description -l pt_BR
Utilitário para sobreposição das ferramentas auto* em buildsystems

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/unsermake
install -m644 *.py *.um %{buildroot}%{_datadir}/unsermake
install -m755 unsermake %{buildroot}%{_datadir}/unsermake

install -m755 %{SOURCE1} -D %{buildroot}/%{_sysconfdir}/profile.d/unsermake.sh

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README COPYING TODO doc/{auug97.pdf,example.obj,unsermake-talk.sxi}
%{_datadir}/%{name}
%{_sysconfdir}/profile.d/*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4-5mdv2010.0
+ Revision: 434547
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4-4mdv2009.0
+ Revision: 261775
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4-3mdv2009.0
+ Revision: 255171
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.4-1mdv2008.1
+ Revision: 140924
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 15 2007 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.4-1mdv2007.0
+ Revision: 121521
- Import unsermake

* Thu May 25 2006 José Melo <mmodem00@gmail.com> 0.4-1mdv2007.1
- Save spec in utf-8
- 0.4

