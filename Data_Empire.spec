Name:           Data_Empire
Version:        1.0
Release:        1%{?dist}
Summary:        A test script

Group:          Utilities
License:        GPL
URL:            https://github.com/nirmalk960/Data_Empire.git
Source0:        Data_Empire-1.0.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


#BuildRequires: 
#Requires:      

%description
A test script inside a simple RPM package


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/Data_Empire
install mytest.sh $RPM_BUILD_ROOT/opt/Data_Empire/Data_Empire.sh


%clean
rm -rf $RPM_BUILD_ROOT


%files
%dir /opt/Data_Empire
%defattr(-,root,root,-)
/opt/Data_Empire/Data_Empire.sh

%post
chmod 755 -R /opt/Data_Empire/
