%define modname pynifti
Name:           python-nifti
URL:            http://niftilib.sf.net/pynifti/
Summary:        Python interface to the NIfTI I/O libraries
Version:        0.20090205.1
Release:        1
License:        MIT License
Group:          Development/Libraries/Python
Source:         %{modname}_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
%if %{defined fedora_version} || %{defined rhel_version} || %{defined centos_version}  
%else  
%{py_requires}  
%endif  
BuildRequires:  python-devel swig nifticlib-devel
BuildRequires:  python-numpy zlib-devel
Requires:       python-numpy nifticlib
BuildRequires:  gcc-c++

%description
Using PyNIfTI one can easily read and write NIfTI and ANALYZE images from
within Python. The NiftiImage class provides Python-style access to the full
header information. Image data is made available via NumPy arrays.

%prep
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(0644,root,root,0755)


%changelog
* Fri Oct 17 2008 - Michael Hanke <michael.hanke@gmail.com> - 0.20081017.1-1
  New upstream version.

* Sat Oct 4 2008 - Michael Hanke <michael.hanke@gmail.com> - 0.20080710.1-1
- Initial release
