<!---
title: 'Arch Linux 설치 체크리스트'
category: Linux
language: Korean
--->

# Arch Linux 설치 체크리스트

개인적인 기준에서 작성한 Arch Linux를 설치할 때의 주의점들이다.
기본적인 설치에 관해서는 [ArchWiki의 가이드](https://wiki.archlinux.org/index.php/Installation_guide)를
따르는 것을 기본으로 한다.

아래에서 설명하는 패키지들을 설치하는 경우는 Live 부트 환경에서 `pacstrap`을 이용하거나,
`arch-chroot`로 마운트한 디스크에서 `pacman`을 이용하면 된다.

- 키보드 레이아웃을 Colemak으로 설정하자. 설치 환경에서 사용할 키맵을 `loadkeys [레이아웃 이름]`을 이용하여 바꿀 수 있다.
Colemak의 `[레이아웃 이름]`은 `colemak`이다.
- `ls /sys/firmware/efi/efivars`를 이용하여 부트 모드가 EFI인지 확인하자. 이에 관해서는 별도의 메인보드 설정이 필요할 수도 있다.
- 인터넷에 접속하자. Wi-Fi를 이용하는 경우에는 `wifi-menu`를 통해 무선랜 네트워크에 접속할 수 있다.
  - 접속이 잘 되었는지 확인하기 위해 아무 사이트([archlinux.org](https://archlinux.org) 등)에 `ping`을 날려보자.
- 시스템 시계를 정확하게 하기 위해 `timedatectl set-ntp true`를 실행한다.
- `fdisk`를 이용하여 Arch Linux를 설치할 디스크를 적절하게 설정해주자. `fdisk -l`을 누르면
디스크의 목록과, `/dev/sdX`와 같이 표시된 디스크들을 확인할 수 있다.
  - EFI 시스템이라면, 512 MiB 정도의 EFI 전용 파티션을 만든다.
  - 메모리의 양에 따라 적절하게 Swap 파티션을 생성한다.
- 파티션을 나누었다면, 포맷해준다. 그리고 모두 마운트한다.
  - EFI 전용 파티션은 FAT32로 포맷한다. `mkfs.fat -F 32 /dev/sdXY`
  - 루트 파티션은 ext4로 포맷한다. `mkfs.ext4 /dev/sdXY`
  - Swap 파티션에 대해서는 `mkswap /dev/sdXY`를 통해 Swap을 설정한 뒤, `swapon /dev/sdXY`를 통해 Swap을 활성화해준다.
  - 루트 파티션은 `/mnt`에 마운트한다. `mount /dev/sdXY /mnt`
  - 부트 파티션(EFI) 파티션은 `/mnt/boot`에 마운트한다. 지금 마운트하지 않으면, 부트 이미지를 설치할 수 없게 된다. `mount /dev/sdXY /mnt/boot`
- 기본 시스템을 다운로드할 미러를 선택하여 시스템을 설치한다.
  - 미러 리스트는 `/etc/pacman.d/mirrorlist`에 있다. 적절하게 우선순위를 바꾸어준다. (`vim`등을 통해)
  - `pacstrap /mnt base linux linux-firmware`으로 `/mnt`에 설치한다.
- 추가적인 소프트웨어들을 다운로드한다.
  - 네트워크 관련: `netctl`, `wpa_supplicant`, `dhcpcd`, `networkmanager`
  - 시스템: `zsh`, `sudo`, `grub`, `efibootmgr`(EFI의 경우)
  - DE, DM: 데스크탑 환경이나 디스플레이 매니저는 원하는 것을 설치한다. `gdm`은 이미 `gnome` 그룹안에 있으므로 `gnome`만을 적어 둠.
  - 기타: `dialog`, `vim`, `man-db`, `man-pages`, `texinfo`
- 디스크가 마운트되어 있는 것을 확인한 뒤, `fstab`을 생성한다. `genfstab -U /mnt >> /mnt/etc/fstab`
- `arch-chroot`로 `/mnt`에 진입한다.
- 시간대를 설정한다. `ln -sf /usr/share/zoneinfo/Region/City /etc/localtime`
- `/etc/adjtime`을 생성한다. `hwclock --systohc`
- 로케일을 생성한다. `/etc/locale.gen`에서 생성할 로케일을 uncomment한다. 그 후 `locale-gen` 실행.
- `/etc/locale.conf`에 사용할 언어에 맞추어 `LANG=en_US.UTF-8` 등을 추가한다.
- `/etc/vconsole.conf`에 사용할 키보드 레이아웃에 맞추어 `KEYMAP=colemak` 등을 추가한다.
- `/etc/hostname`을 수정하여 호스트네임을 설정한다.
- `/etc/hosts` 파일을 수정한다. `127.0.0.1`, `127.0.1.1`, `::1` 항목을 추가하자.
- `passwd`를 실행하여 `root` 계정의 패스워드를 설정한다.
- `useradd -m -G superusers -s /bin/zsh [계정명]` 과 같이 `root` 계정이 아닌, 관리자 계정을 만들자.
  - 계정을 만든 뒤에는 `passwd [계정명]`을 입력하여 패스워드를 설정한다.
  - `/etc/sudoers` 파일을 `visudo`로 수정하여 관리자 그룹을 추가하도록 하자. `%superusers`와 같이
  항목을 추가하면 된다.
- 부트로더를 설치하자. 여기서는 GRUB을 설치할 것이다.
  - `grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB`, `--efi-directory`에는
  부트 파티션이 어디에 마운트되어 있는지 확인한 뒤 옵션을 추가하자.
  - 설치가 끝났다면 설정파일을 생성하여 부트 파티션에 저장하자. `grub-mkconfig -o /boot/grub/grub.cfg`
- `exit`으로 `arch-chroot`에서 나온다. `reboot`으로 설치된 디스크를 통해 재부팅한다.
- 관리자 계정으로 로그인하여 필요한 서비스를 활성화하자.
  - Bluetooth의 경우는 `systemd enable bluetooth.service`
  - NetworkManager의 경우는 `systemd enable NetworkManager.service`
  - GDM의 경우는 `systemd enable gdm.service`
- 이제 재부팅하면, GDM의 로그인 화면이 반겨줄 것이다.
