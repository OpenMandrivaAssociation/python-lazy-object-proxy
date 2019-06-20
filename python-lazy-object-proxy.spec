%define module	lazy-object-proxy
  
Summary:	A fast and thorough lazy object proxy
Name:		python-lazy-object-proxy
Version:	1.4.1
Release:	3
Group:		Development/Python
License:	BSD
Url:		https://pypi.python.org/pypi/lazy-object-proxy
Source0:	https://github.com/ionelmc/python-lazy-object-proxy/archive/v%{version}.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
 
%description 
A common base representation of python source code for pylint
and other projects

%prep
%setup -q
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot} --record=FILE_LIST

%files
%{py_platsitedir}/lazy_object_proxy
%{py_platsitedir}/lazy_object_proxy*.egg-info
