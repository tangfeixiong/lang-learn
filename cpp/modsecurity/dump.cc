


#include <unistd.h>
#include <stdio.h>
#include <string.h>


#include <modsecurity/modsecurity.h>
#include <modsecurity/rules.h>
#include <modsecurity/rule_message.h>


#include <string>
#include <memory>

char rules_file[] = "/Users/fanhongling/Downloads/workspace/src/github.com/SpiderLabs/owasp-modsecurity-crs/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf";

int main(int argc, char **argv) {
    modsecurity::ModSecurity *modsec;
    modsecurity::Rules *rules;
    modsecurity::ModSecurityIntervention it;
//    ModSecurity::Transaction trans;

//    if (argc < 2) {
//        std::cout << "Use " << *argv << " test-case-file.conf";
//        std::cout << std::endl << std::endl;
//        return -1;
//    }
//    *(argv++);

//    std::string rules_arg(*argv);

    modsec = new modsecurity::ModSecurity();
    
    rules = new modsecurity::Rules();
    
    if (rules->loadFromUri(rules_file) < 0) {
        std::cout << "Problems loading the rules..." << std::endl;
        std::cout << rules->m_parserError.str() << std::endl;
        return -1;
    }
    rules->dump();
    
//    Transaction *modsecTransaction = new Transaction(modsec, rules);
    
//    modsecTransaction->processConnection("127.0.0.1");
//    if (modsecTransaction->intervention()) {
//       std::cout << "There is an intervention" << std::endl;
//    }
}