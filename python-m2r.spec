Summary:	Converts markdown files including rst to a valid rst format
Name:		python-m2r
Version:	0.2.1
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/m2r/
Source0:	https://files.pythonhosted.org/packages/39/e7/9fae11a45f5e1a3a21d8a98d02948e597c4afd7848a0dbe1a1ebd235f13e/m2r-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildArch:	noarch

%description
Converts markdown files including rst to a valid rst format

%package -n python2-m2r
Summary:	Converts markdown files including rst to a valid rst format
Group:		Development/Python

%description -n python2-m2r
Converts markdown files including rst to a valid rst format

%prep
%setup -qn m2r-%{version}
%apply_patches

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/m2r.py*
%{py_sitedir}/*.egg-info
%{py_sitedir}/__pycache__/*
%{_bindir}/m2r

%files -n python2-m2r
%{py2_puresitedir}/m2r.py*
%{py2_puresitedir}/*.egg-info
