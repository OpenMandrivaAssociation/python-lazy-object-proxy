%global debug_package %{nil}
%define module lazy-object-proxy
%define oname lazy_object_proxy

Name:		python-lazy-object-proxy
Summary:	A fast and thorough lazy object proxy
Version:	1.12.0
Release:	1
Group:		Development/Python
License:	BSD
URL:		https://github.com/ionelmc/python-lazy-object-proxy
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description 
A common base representation of python source code for pylint
and other projects

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%files
%doc README.rst
%{python_sitearch}/%{oname}
%{python_sitearch}/%{oname}-%{version}.dist-info
