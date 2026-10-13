Summary:	Converts markdown files including rst to a valid rst format
Name:		python-m2r
Version:	2.1.0
Release:	1
License:	MIT
Group:		Development/Python
# Old Url:		https://pypi.org/project/m2r/
Url:		https://pypi.org/project/m2r2/
Source0:	https://files.pythonhosted.org/packages/source/m/m2r2/m2r2-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(wheel)
BuildArch:	noarch

%description
Converts markdown files including rst to a valid rst format

%install -a
ln -s m2r2 %{buildroot}%{_bindir}/m2r
# Keep the historical import name. m2r2 re-exports convert and M2R.
echo 'from m2r2 import *' > %{buildroot}%{py_sitedir}/m2r.py

%files
%license LICENSE
%doc README.md
%{py_sitedir}/m2r.py
%{py_sitedir}/__pycache__/m2r.cpython-*.pyc
%{py_sitedir}/m2r2
%{py_sitedir}/m2r2-%{version}.dist-info
%{_bindir}/m2r
%{_bindir}/m2r2
