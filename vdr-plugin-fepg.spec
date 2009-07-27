
%define plugin	fepg
%define name	vdr-plugin-%plugin
%define version	0.4.1
%define rel	2

Summary:	VDR plugin: A Graphical EPG
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		http://fepg.org/
Source:		http://fepg.org/files/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
fEPG is a plugin for VDR that provides a graphical way of viewing and
navigating through EPG data.

%prep
%setup -q -n %plugin-%version
chmod a-x README HISTORY
%vdr_plugin_prep

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
