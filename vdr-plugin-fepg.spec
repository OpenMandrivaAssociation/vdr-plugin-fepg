
%define plugin	fepg
%define name	vdr-plugin-%plugin
%define version	0.2.1
%define rel	9

Summary:	VDR plugin: A Graphical EPG
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://fepg.tk/
Source:		http://fepg2.f2g.net/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
fEPG is a plugin for VDR that provides a graphical way of viewing and
navigating through EPG data.

%prep
%setup -q -n %plugin-%version
chmod a-x README HISTORY

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


