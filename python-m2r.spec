Summary:	Converts markdown files including rst to a valid rst format
Name:		python-m2r
Version:	0.2.1
Release:	3
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/m2r/
Source0:	https://files.pythonhosted.org/packages/39/e7/9fae11a45f5e1a3a21d8a98d02948e597c4afd7848a0dbe1a1ebd235f13e/m2r-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
Converts markdown files including rst to a valid rst format

%prep
%autosetup -p1 -n m2r-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/m2r.py*
%{py_sitedir}/*.egg-info
%{_bindir}/m2r
