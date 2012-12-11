%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: A powerful retail system
Name:    stoq
Version: 1.0.0
Release: 3
License: GPL
Group: System/Libraries
URL: http://www.stoq.com.br/
Source: stoq-%{version}.tar.gz
Requires: postgresql >= 8.4
Requires: pygtk2 >= 2.16
Requires: pypoppler >= 0.12.1
Requires: python-dateutil >= 1.4.1
Requires: python-imaging >= 1.1.5
Requires: python-gudev >= 147
Requires: python-kiwi >= 1.9.29
Requires: python-mako >= 0.2.5
Requires: python-psycopg2 >= 2.0.5
Requires: python-reportlab >= 2.4
Requires: python-zope-interface >= 3.0.1
BuildRequires: python-kiwi >= 1.9.28
BuildRequires: python-devel
BuildArch: noarch

%description
Stoq is a suite of Retail Management System applications.
It includes the following applications;
Point of Sales, Cash register, Sales, Purchase Orders, Inventory control,
Customer Relationship Management (CRM), Financial Accounting, 
Accounts Payable and Accounts Receivable, Printable Reports, Employees 
and Suppliers registry.

%prep
%setup -q -n stoq-%{version}

%build
%{__python} setup.py build

%install
mkdir -p %{_etcdir}/stoq
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_defaultdocdir}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS CONTRIBUTORS COPYING README NEWS
%{_bindir}/stoq
%{_bindir}/stoqcreatedbuser
%{_bindir}/stoqdbadmin
%{_bindir}/stoqruncmd
%{_sysconfdir}/stoq
%{_datadir}/locale/*/LC_MESSAGES/stoq.mo
%{_datadir}/stoq/*
%{_datadir}/polkit-1/*
%{_datadir}/icons/*
/usr/lib/stoqlib/*
%{_datadir}/applications/stoq.desktop
/usr/lib/python2.7/site-packages/*


%changelog
* Fri Jul 29 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.0.0-2mdv2012.0
+ Revision: 692304
- bump new version
- doc directory changed
- first package version on mdv
- Created package structure for stoq.

