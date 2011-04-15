%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define name stoq
%define version 0.9.15
%define release %mkrel 2

Summary: A powerful retail system
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Libraries
URL: http://www.stoq.com.br/
Source: stoq-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-kiwi >= 1.9.24, stoqlib >= 0.9.15, python-reportlab, python-psycopg2
BuildRequires: python-kiwi >= 1.9.27, stoqlib >= 0.9.15
BuildRequires: python-devel
BuildArch: noarch

%description
Stoq is an advanced retails system which has as main goals the
usability, good devices support, and useful features for retails.

%prep
%setup -q -n stoq-%{version}

%build
%{__python} setup.py build

%install
mkdir -p %{_etcdir}/stoq
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}%{_defaultdocdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CONTRIBUTORS COPYING README NEWS
%{_bindir}/stoq
%{_bindir}/stoqdbadmin
%{_bindir}/stoqruncmd
%{_sysconfdir}/stoq
%{_datadir}/locale/*/LC_MESSAGES/stoq.mo
%{_datadir}/stoq/glade
%{_datadir}/stoq/pixmaps
%{_datadir}/applications/stoq.desktop
%{python_sitelib}/stoq
/usr/lib/python2.6/site-packages/stoq-0.9.15-py2.6.egg-info
