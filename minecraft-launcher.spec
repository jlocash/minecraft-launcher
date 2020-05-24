Name:           minecraft-launcher
Version:        2.1.14403
Release:        1%{?dist}
Summary:        Minecraft Launcher
License:        Proprietary
URL:            https://minecraft.net

Source0:        https://launcher.mojang.com/download/linux/x86_64/%{name}_%{version}.tar.gz
Source1:        minecraft-launcher.desktop
Source2:        https://launcher.mojang.com/download/minecraft-launcher.svg

Requires:	    java-1.8.0-openjdk

%description
Minecraft Launcher

%install
install -d %{buildroot}/opt/
tar -xzvf %{SOURCE0} -C %{buildroot}/opt/

install -d -m 0755 %{buildroot}%{_datadir}/applications
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/%{name}.svg 

%files
/opt/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/symbolic/apps/%{name}.svg 

%changelog
* Sun May 24 2020 Joshua Locash <locashjosh@gmail.com> - 2.1.14403-1
- new version

* Sun Jan 26 2020 Joshua Locash <locashjosh@gmail.com> - 2.1.11314-1
- bump to v2.1.11314

* Sat Jan 18 2020 Joshua Locash <locashjosh@gmail.com> - 2.1.10835-1
- new version

