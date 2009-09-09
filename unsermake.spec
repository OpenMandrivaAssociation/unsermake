Name:		unsermake
Version:	0.4
Release:	%mkrel 5
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


