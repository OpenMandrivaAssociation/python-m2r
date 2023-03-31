Summary:	Converts markdown files including rst to a valid rst format
Name:		python-m2r
Version:	0.3.2
Release:	2
License:	MIT
Group:		Development/Python
# Old Url:		https://pypi.org/project/m2r/
Url:		https://pypi.org/project/m2r2/
Source0:	https://files.pythonhosted.org/packages/source/m/m2r2/m2r2-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Converts markdown files including rst to a valid rst format

%prep
%autosetup -p1 -n m2r2-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

ln -s m2r2 %{buildroot}%{_bindir}/m2r
ln -s m2r2.py %{buildroot}%{py_sitedir}/m2r.py
cp -a %{buildroot}%{py_sitedir}/m2r2-%{version}-py%{python_version}.egg-info %{buildroot}%{py_sitedir}/m2r-%{version}-py%{version}.egg-info
find %{buildroot}%{py_sitedir}/m2r-%{version}-py%{version}.egg-info -type f |xargs sed -i -e 's,m2r2,m2r,g'

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/m2r.py*
%{py_sitedir}/m2r2.py*
%{py_sitedir}/*.egg-info
%{_bindir}/m2r
%{_bindir}/m2r2
