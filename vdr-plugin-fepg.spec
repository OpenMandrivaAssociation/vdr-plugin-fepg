%define plugin	fepg

Summary:	VDR plugin: A Graphical EPG
Name:		vdr-plugin-%plugin
Version:	0.4.1
Release:	5
Group:		Video
License:	GPLv2+
URL:		https://fepg.org/
Source:		http://fepg.org/files/vdr-%plugin-%version.tgz
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.4.1-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 396102
- new version
- drop duplicate-param-name.patch, fixed upstream
- license now GPLv2+

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.4.0-3mdv2009.1
+ Revision: 359705
- fix typo in function declaration (duplicate-param-name.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.4.0-2mdv2009.0
+ Revision: 197930
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.4.0-1mdv2009.0
+ Revision: 197669
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.3.1-3mdv2008.1
+ Revision: 145096
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.3.1-2mdv2008.1
+ Revision: 103095
- rebuild for new vdr

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0.3.1-1mdv2008.0
+ Revision: 81906
- 0.3.1
- adapt license tag to the new policy

* Thu Jul 19 2007 Anssi Hannula <anssi@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 53420
- 0.3.0
- better URL

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1-11mdv2008.0
+ Revision: 50001
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1-10mdv2008.0
+ Revision: 42087
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.2.1-9mdv2008.0
+ Revision: 22673
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-8mdv2007.0
+ Revision: 90924
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-7mdv2007.1
+ Revision: 74015
- rebuild for new vdr
- Import vdr-plugin-fepg

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-2mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.2.1-1mdv2007.0
- initial Mandriva release

