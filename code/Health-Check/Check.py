import datetime
import subprocess
import time
import psutil


def check_and_run_process():
    now = datetime.datetime.now()
    start_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = now.replace(hour=9, minute=10, second=0, microsecond=0)

    cvedia_process_name = "cvediart.exe"
    java_process_name = "java.exe"

    cvedia_path = "CVEDIA-RT.bat"
    jar_path = "Z:\\Github\\Project\\SK-Gas\\build\\libs\\bridge.jar"

    while True:
        now = datetime.datetime.now()
        if start_time <= now <= end_time:
            # 현재 실행 중인 프로세스 목록에서 CVEDIA-RT.exe와 java.exe가 실행 중인지 확인
            cvedia_running = any(cvedia_process_name in p.name() for p in psutil.process_iter())
            java_running = any(java_process_name in p.name() for p in psutil.process_iter())

            if not cvedia_running:
                startupinfo = subprocess.STARTUPINFO()
                subprocess.Popen([cvedia_path], startupinfo=startupinfo, shell=True)
                print("CVEDIA-RT 실행")

            if not java_running:
                startupinfo = subprocess.STARTUPINFO()
                subprocess.Popen(f'java -jar {jar_path}', startupinfo=startupinfo, shell=True)
                print("Bridge 실행")

        elif now > end_time:
            for proc in psutil.process_iter():
                if proc.name() == cvedia_process_name or proc.name() == java_process_name:
                    proc.kill()
                    print(f"{proc.name()} 프로세스 종료")

            print(f"운영시간이 아닙니다 - 운영시간 : {str(start_time)[11:16]} ~ {str(end_time)[11:16]}")
            time.sleep(60)
            continue

        time.sleep(10)

if __name__ == "__main__":
    check_and_run_process()
