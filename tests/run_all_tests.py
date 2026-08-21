import subprocess
import sys



TESTS = [

    "tests.test_config",

    "tests.test_logger",

    "tests.test_runtime_status",

    "tests.test_session_manager",

    "tests.test_sync_persistence",

    "tests.test_aios_v1_e2e",

"tests.test_brain_interface",

"tests.test_mobile_brain_bridge",

"tests.test_llm_brain",

"tests.test_provider_layer",

"tests.test_real_provider_chain"

]



print(
    "===== AI-OS V1.0 RC1 Test Suite ====="
)



failed = []



for test in TESTS:


    print()

    print(
        "Running:",
        test
    )


    result = subprocess.run(

        [
            sys.executable,
            "-m",
            test
        ]

    )


    if result.returncode != 0:


        failed.append(test)



print()



if failed:


    print(
        "FAILED:"
    )


    for item in failed:

        print(item)



    sys.exit(1)



else:


    print(
        "===== ALL TESTS PASSED ====="
    )

