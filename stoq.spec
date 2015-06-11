Summary:	A powerful retail system
Name:		stoq
Version:	1.9.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.stoq.com.br/
Source0:	%{version}.tar.gz
BuildRequires:	python-kiwi >= 1.9.28
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python2)
Requires:	postgresql >= 8.4
Requires:	pygtk2 >= 2.16
Requires:	pypoppler >= 0.12.1
Requires:	python-dateutil >= 1.4.1
Requires:	python-imaging >= 1.1.5
Requires:	python-gudev >= 147
Requires:	python-kiwi >= 1.9.29
Requires:	python-mako >= 0.2.5
Requires:	python-psycopg2 >= 2.0.5
Requires:	python-reportlab >= 2.4
Requires:	python-zope-interface >= 3.0.1
BuildArch:	noarch

%description
Stoq is a suite of Retail Management System applications.
It includes the following applications;
Point of Sales, Cash register, Sales, Purchase Orders, Inventory control,
Customer Relationship Management (CRM), Financial Accounting,
Accounts Payable and Accounts Receivable, Printable Reports, Employees
and Suppliers registry.

%files -f %{name}.lang
%doc AUTHORS CONTRIBUTORS COPYING README NEWS
%{_bindir}/stoq
%{_bindir}/stoqcreatedbuser
%{_bindir}/stoqdbadmin
%{_bindir}/stoqruncmd
%{_bindir}/stoq-daemon
%{_datadir}/gnome/help/stoq
%{_sysconfdir}/stoq
%{_datadir}/stoq/*
%{_datadir}/polkit-1/*
%{_datadir}/icons/*
%{_prefix}/lib/stoqlib/*
%{_datadir}/applications/stoq.desktop
%{python2_sitelib}/*

#----------------------------------------------------------------------------

%prep
%setup -q -n stoq-%{version}

%build
%{__python2} setup.py build

%install
mkdir -p %{buildroot}%{_sysconfdir}/stoq
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_defaultdocdir}

%find_lang %{name}

